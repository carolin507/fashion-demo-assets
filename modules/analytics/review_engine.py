import os
import re
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
from tqdm import tqdm

# ============================
# NLP 初始化
# ============================

# VADER
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

# spaCy：只載 tokenizer + POS
try:
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner", "lemmatizer"])
except Exception:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner", "lemmatizer"])


# ============================
# 基本清理（順便避免空 token）
# ============================
def clean_text(text):
    text = text.lower()
    text = text.encode("ascii", "ignore").decode()  # remove emoji
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


class ReviewEngine:
    def __init__(self, data_path="data/raw/reviews/reviews.csv"):
        self.data_path = data_path
        self.df = pd.read_csv(self.data_path)
        self.clean_data()

    # -------------------------------
    # Step 1: 清理欄位
    # -------------------------------
    def clean_data(self):
        df = self.df.copy()

        df.rename(
            columns={
                "Review Text": "review",
                "Rating": "rating",
                "Recommended IND": "recommended",
                "Positive Feedback Count": "positive_feedback",
            },
            inplace=True,
        )

        df["review"] = df["review"].fillna("").astype(str)
        df["review"] = df["review"].apply(clean_text)

        df["rating"] = df["rating"].fillna(0).astype(int)
        df["review_length"] = df["review"].str.len()

        self.df = df

    # -------------------------------
    # Step 2: 情緒標記
    # -------------------------------
    def add_sentiment(self):
        sia = SentimentIntensityAnalyzer()
        df = self.df.copy()

        df["sentiment_score_raw"] = df["review"].apply(
            lambda x: sia.polarity_scores(x)["compound"]
        )

        def classify(row):
            score = row["sentiment_score_raw"]
            rating = row["rating"]

            if rating >= 4:
                return "Positive"
            if rating <= 2:
                return "Negative"

            if score >= 0.2:
                return "Positive"
            if score <= -0.2:
                return "Negative"
            return "Neutral"

        df["sentiment_label"] = df.apply(classify, axis=1)
        self.df = df

    # -------------------------------
    # Step 3: 關鍵字萃取（ADJ + NOUN）
    # -------------------------------
    def extract_keywords(self, top_n=50, min_review_length=5):

        # Ensure sentiment is computed before keyword extraction
        if "sentiment_label" not in self.df.columns:
            self.add_sentiment()

        # Safety: rebuild sentiment labels if they are still missing (e.g., caller
        # skipped add_sentiment or loaded a pre-cleaned df without labels).
        if "sentiment_label" not in self.df.columns:
            fallback_df = self.df.copy()
            if "rating" in fallback_df.columns:
                fallback_df["sentiment_label"] = fallback_df["rating"].apply(
                    lambda r: "Positive" if r >= 4 else ("Negative" if r <= 2 else "Neutral")
                )
            else:
                fallback_df["sentiment_label"] = "Neutral"
            self.df = fallback_df

        df = self.df[self.df["review_length"] >= min_review_length].copy()

        # Broaden filters so we do not drop too many reviews when data is sparse
        pos_df = df[df["sentiment_label"] == "Positive"]
        neg_df = df[df["sentiment_label"] == "Negative"]

        # Fallback to rating-based slices if sentiment labels are missing or empty
        if pos_df.empty and "rating" in df.columns:
            pos_df = df[df["rating"] >= 4]
        if neg_df.empty and "rating" in df.columns:
            neg_df = df[df["rating"] <= 2]

        # 主觀外觀形容詞避免放進 Negative
        positive_style_words = {
            "cute",
            "pretty",
            "beautiful",
            "nice",
            "lovely",
            "gorgeous",
            "stylish",
            "flattering",
        }

        # 針對實質面負面形容詞
        negative_adj_words = {
            "small",
            "tight",
            "itchy",
            "thin",
            "cheap",
            "shapeless",
            "uncomfortable",
            "loose",
            "big",
            "huge",
            "sheer",
            "transparent",
            "scratchy",
            "bad",
            "poor",
        }

        # 痛點名詞（常見 VOC）
        pain_nouns_set = {
            "fit",
            "size",
            "material",
            "quality",
            "fabric",
            "support",
            "stitching",
            "waist",
            "color",
            "length",
        }

        POS_ADJ = []
        NEG_ADJ = []
        NEG_NOUN = []

        # ----------------------
        # Positive ADJ
        # ----------------------
        print("\nExtracting Positive adjectives...")
        for doc in tqdm(
            nlp.pipe(pos_df["review"], batch_size=200),
            total=len(pos_df),
            ncols=90,
        ):
            for t in doc:
                if t.pos_ == "ADJ" and len(t.lemma_) > 1:
                    if t.lemma_ not in negative_adj_words:
                        POS_ADJ.append(t.lemma_)

        # ----------------------
        # Negative ADJ + NOUN
        # ----------------------
        print("\nExtracting Negative adjectives and pain-point nouns...")
        for doc in tqdm(
            nlp.pipe(neg_df["review"], batch_size=200),
            total=len(neg_df),
            ncols=90,
        ):
            for t in doc:

                # 形容詞側重產品痛點
                if t.pos_ == "ADJ" and len(t.lemma_) > 1:
                    if t.lemma_ not in positive_style_words:
                        NEG_ADJ.append(t.lemma_)

                # 痛點名詞
                if t.pos_ == "NOUN" and len(t.lemma_) > 1:
                    if t.lemma_ in pain_nouns_set:
                        NEG_NOUN.append(t.lemma_)

        # 統計
        pos_adj_df = pd.Series(POS_ADJ).value_counts().reset_index()
        pos_adj_df.columns = ["word", "count"]
        pos_adj_df["sentiment"] = "Positive_ADJ"

        neg_adj_df = pd.Series(NEG_ADJ).value_counts().reset_index()
        neg_adj_df.columns = ["word", "count"]
        neg_adj_df["sentiment"] = "Negative_ADJ"

        neg_noun_df = pd.Series(NEG_NOUN).value_counts().reset_index()
        neg_noun_df.columns = ["word", "count"]
        neg_noun_df["sentiment"] = "Negative_NOUN"

        # 合併並保留前 top_n
        frames = []
        for df_slice in (pos_adj_df, neg_adj_df, neg_noun_df):
            if not df_slice.empty:
                frames.append(df_slice.head(top_n))

        if frames:
            self.keywords = pd.concat(frames, ignore_index=True)
        else:
            self.keywords = pd.DataFrame(columns=["word", "count", "sentiment"])

        return self.keywords

    # -------------------------------
    # Step 4: 輸出
    # -------------------------------
    def export_processed(self, out_dir="data/processed/reviews"):
        os.makedirs(out_dir, exist_ok=True)

        self.df.to_csv(os.path.join(out_dir, "reviews_processed.csv"), index=False)
        self.keywords.to_csv(os.path.join(out_dir, "review_keywords.csv"), index=False)

        print("\nReview processed files exported successfully!")

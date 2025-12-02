import pandas as pd
import numpy as np

pattern_labels = ["Solid", "Striped", "Floral", "Plaid", "Spotted"]

color_labels = [
    "Black", "Gray", "White", "Beige", "Orange", "Pink",
    "Red", "Green", "Brown", "Blue", "Yellow", "Purple"
]

top_categories = [
    "Top", "T-Shirt", "Shirt", "Cardigan", "Blazer",
    "Sweatshirt", "Vest", "Jacket", "Coat", "Dress"
]

bottom_categories = ["Skirt", "Pants", "Jeans", "Shorts", "Dress"]

def build_image_url(photo_filename: str) -> str:
    base = (
        "https://raw.githubusercontent.com/carolin507/"
        "fashion-demo-assets/main/assets/streetstyle/"
    )
    return base + str(photo_filename)

def build_pairs(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for _, row in df.iterrows():

        labels = [x.strip() for x in str(row["v_labels"]).split(",")]

        # 1) Pattern
        pattern = next((x for x in labels if x in pattern_labels), np.nan)

        # 2) Colors
        colors = [x for x in labels if x in color_labels]
        top_color = colors[0] if len(colors) > 0 else np.nan
        bottom_color = colors[1] if len(colors) > 1 else top_color

        # 3) Category extraction
        category_candidates = [
            x for x in labels
            if x not in color_labels and x not in pattern_labels
        ]

        if len(category_candidates) == 1:
            top_cat = bottom_cat = category_candidates[0]
        else:
            tops = [x for x in labels if x in top_categories]
            bottoms = [x for x in labels if x in bottom_categories]

            top_cat = tops[0] if len(tops) > 0 else np.nan
            bottom_cat = bottoms[0] if len(bottoms) > 0 else np.nan

            if pd.isna(top_cat) and not pd.isna(bottom_cat):
                top_cat = bottom_cat
            if pd.isna(bottom_cat) and not pd.isna(top_cat):
                bottom_cat = top_cat

            if pd.isna(top_cat) and pd.isna(bottom_cat):
                top_cat = bottom_cat = (
                    category_candidates[0] if len(category_candidates) else np.nan
                )

        # ⭐⭐⭐ NEW: 組合 recommender 需要的 dict ⭐⭐⭐
        top_dict = {
            "color": top_color,
            "style": pattern,
            "category": top_cat,
        }

        bottom_dict = {
            "color": bottom_color,
            "style": pattern,
            "category": bottom_cat,
        }

        # ---------------------------
        rows.append({
            "full_image_url": build_image_url(row["photo"]),

            # 原欄位（保持相容性）
            "top_color": top_color,
            "top_category": top_cat,
            "top_pattern": pattern,
            "bottom_color": bottom_color,
            "bottom_category": bottom_cat,
            "bottom_pattern": pattern,

            # 新增 recommender 需要的欄位！
            "top": top_dict,
            "bottom": bottom_dict,

            "top_url": "",
            "bottom_url": "",
        })

    return pd.DataFrame(rows)



# ====== Main ======

def main():
    df = pd.read_csv("data/df_pairs.csv")
    pairs = build_pairs(df)

    output = "data/pairs_from_vlabels.csv"
    pairs.to_csv(output, index=False)

    print("✔ 完成：", output)
    print("✔ 輸出筆數：", len(pairs))


if __name__ == "__main__":
    main()

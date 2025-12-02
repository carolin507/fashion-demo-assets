# modules/ai_models/clip_classifier.py
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Dict, List, Tuple

import torch
import clip
from PIL import Image

from modules.ai_models.base_model import BaseFashionModel


# ------------------------------------------------------------
# 基本標籤（先用你們現在這組，之後可以再調整）
# ------------------------------------------------------------

COLOR_LABELS = [
    "Black",
    "Gray",
    "White",
    "Beige",
    "Orange",
    "Pink",
    "Red",
    "Green",
    "Brown",
    "Blue",
    "Yellow",
    "Purple",
]

STYLE_LABELS = ["Solid", "Striped", "Floral", "Plaid", "Spotted"]

CATEGORY_LABELS = [
    "Top",
    "T-Shirt",
    "Shirt",
    "Cardigan",
    "Blazer",
    "Sweatshirt",
    "Vest",
    "Jacket",
    "Dress",
    "Coat",
    "Skirt",
    "Pants",
    "Jeans",
    "Jumpsuit",
    "Sweater",
]

BODY_PART_LABELS = ["upper body clothing", "lower body clothing"]


class ClipClassifier(BaseFashionModel):
    """
    使用 OpenAI CLIP 做：
    - 顏色辨識
    - 花紋 / 紋理辨識
    - 類別辨識
    - 上半身 / 下半身判斷
    """

    def __init__(self) -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = device

        # 1. 下載 / 載入 CLIP 模型與預處理
        self.model, self.preprocess = clip.load("ViT-B/32", device=device)

        # 2. 預先把文字標籤轉成 embedding
        self.color_text_feats = self._compute_text_features(COLOR_LABELS)
        self.category_text_feats = self._compute_text_features(CATEGORY_LABELS)
        self.style_text_feats = self._compute_text_features(STYLE_LABELS)
        self.part_text_feats = self._compute_text_features_for_parts(BODY_PART_LABELS)

    # ----------------- 文字 embedding -----------------

    def _compute_text_features(self, labels: List[str]) -> torch.Tensor:
        """將一組 clothing label 轉成 text embedding。"""
        prompts = [f"a photo of a {label} clothing" for label in labels]
        tokens = clip.tokenize(prompts).to(self.device)
        with torch.no_grad():
            text_feats = self.model.encode_text(tokens)
        text_feats /= text_feats.norm(dim=-1, keepdim=True)
        return text_feats  # [L, 512]

    def _compute_text_features_for_parts(self, labels: List[str]) -> torch.Tensor:
        """上 / 下身的描述不用加 clothing 字樣。"""
        tokens = clip.tokenize(labels).to(self.device)
        with torch.no_grad():
            text_feats = self.model.encode_text(tokens)
        text_feats /= text_feats.norm(dim=-1, keepdim=True)
        return text_feats

    # ----------------- 圖片 embedding -----------------

    def _image_to_features(self, image: Image.Image) -> torch.Tensor:
        """PIL Image → CLIP image embedding ([1,512])。"""
        img_input = self.preprocess(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            img_feats = self.model.encode_image(img_input)
        img_feats /= img_feats.norm(dim=-1, keepdim=True)
        return img_feats

    # ----------------- top-k label 工具 -----------------

    @staticmethod
    def _top_k_labels(
        image_feat: torch.Tensor,
        text_feats: torch.Tensor,
        labels: List[str],
        k: int = 1,
        threshold: float = 0.20,
    ) -> List[Tuple[str, float]]:
        """
        image_feat: [1,512]
        text_feats: [L,512]
        return: [(label, score), ...]
        """
        sims = image_feat @ text_feats.T  # [1, L]
        sims = sims[0]

        topk_scores, topk_idx = torch.topk(sims, k)
        results: List[Tuple[str, float]] = []

        for score, idx in zip(topk_scores, topk_idx):
            score_val = float(score.item())
            if score_val < threshold:
                results.append(("Unknown", score_val))
            else:
                results.append((labels[int(idx)], score_val))

        return results

    # ----------------- 對外主函式：analyze() -----------------

    def analyze(self, image: Image.Image) -> Dict[str, str]:
        """
        符合 BaseFashionModel 介面：
        輸入 PIL Image，回傳顏色 / 花紋 / 類別 / 上下身 part。

        回傳格式：
        {
            "color": ...,
            "style": ...,
            "category": ...,
            "part": "Top" or "Bottom"
        }
        """
        image_feats = self._image_to_features(image)

        color_top3 = self._top_k_labels(
            image_feats, self.color_text_feats, COLOR_LABELS, k=3
        )
        category_top = self._top_k_labels(
            image_feats, self.category_text_feats, CATEGORY_LABELS, k=1
        )
        style_top = self._top_k_labels(
            image_feats, self.style_text_feats, STYLE_LABELS, k=1
        )
        part_top = self._top_k_labels(
            image_feats, self.part_text_feats, BODY_PART_LABELS, k=1
        )

        result: Dict[str, str] = {}

        # 顏色
        result["color"] = color_top3[0][0]

        # 花紋 / 紋理
        result["style"] = style_top[0][0]

        # 類別
        result["category"] = category_top[0][0]

        # 上 / 下身
        part_label = part_top[0][0]
        if part_label == "upper body clothing":
            result["part"] = "Top"
        elif part_label == "lower body clothing":
            result["part"] = "Bottom"
        else:
            result["part"] = "Top"  # 預設當作上半身

        return result
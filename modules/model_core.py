# modules/model_core.py
# -*- coding: utf-8 -*-

"""
model_core.py

這是「AI 模組的 orchestrator / 控制中心」。

負責：
1. 呼叫影像分析模型（目前預設使用 CLIP → ClipClassifier）
2. 呼叫共現推薦系統（CoOccurrenceRecommender）
3. 對外提供兩個主要 API：
    - infer_labels(image) → 圖片分析（不含推薦）
    - infer_and_recommend(image, recommender) → 圖片分析 + 推薦

架構採 plugin 設計：
未來只要把 ClipClassifier 換成 YOLOSegmentor / EPyNetModel，
前端與推薦系統都不需要跟著改。
"""

from __future__ import annotations

from typing import Dict
from PIL import Image
import pandas as pd

# ---- AI 模型（可替換：CLIP / YOLO / EPYNET ...） ----
from modules.ai_models.clip_classifier import ClipClassifier

# ---- 推薦系統（你們的共現模組） ----
from modules.cooccurrence_recommender import (
    CoOccurrenceRecommender,
)


# ============================================================
# 1) 目前使用的 AI 模型（ClipClassifier）
#    ※ 未來要換模型，只要改這一行
# ============================================================

_fashion_model = ClipClassifier()   # ← 換模型只要改這裡！


# ============================================================
# 2) 圖片 → labels（顏色 / 花紋 / 類別 / 上下身）
# ============================================================

def infer_labels(image: Image.Image) -> Dict[str, str]:
    """
    給前端與 inference.py 使用的標準入口：

    輸入：
        PIL.Image

    回傳：
    {
        "color": <str>,
        "style": <str>,
        "category": <str>,
        "part": "Top" | "Bottom"
    }
    """
    return _fashion_model.analyze(image)


# ============================================================
# 3) 推薦系統：整合「影像辨識 + 共現推薦」
# ============================================================

def infer_and_recommend(
    image: Image.Image,
    recommender: CoOccurrenceRecommender,
    k: int = 3,
) -> Dict:
    """
    一次完成：
    1) 用 AI 模型做影像辨識
    2) 根據 part 決定推薦方向（Top→Bottom 或 Bottom→Top）

    回傳格式：
    {
        "input_label": {
            "color": ...,
            "style": ...,
            "category": ...,
            "part": ...
        },
        "direction": "Top_to_Bottom" | "Bottom_to_Top",
        "recommendations": [ {...}, {...}, ... ]   # list 長度 ≤ k
    }
    """
    labels = _fashion_model.analyze(image)

    item = {
        "color": labels["color"],
        "style": labels["style"],
        "category": labels["category"],
    }

    # ---- 根據 part 決定推薦方向 ----
    if labels["part"] == "Top":
        recs = recommender.recommend_from_top(item, k=k)
        direction = "Top_to_Bottom"
    else:
        recs = recommender.recommend_from_bottom(item, k=k)
        direction = "Bottom_to_Top"

    return {
        "input_label": labels,
        "direction": direction,
        "recommendations": recs,
    }


# ============================================================
# 4) RichWear → pair dataset（預留給你們後處理）
#    ※ 這部分我保留簡化版，供推薦系統初始化使用
# ============================================================

def build_recommender_from_pairs(df_pairs: pd.DataFrame) -> CoOccurrenceRecommender:
    """
    給主程式或 dashboard 使用：
    用 top-bottom pair 資料建立共現推薦器。
    """
    return CoOccurrenceRecommender(df_pairs)

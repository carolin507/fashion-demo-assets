# modules/inference.py
import random
from modules.utils import color_labels, pattern_labels, category_labels

def predict_labels(image, gender):
    """目前為 Mock，未來可換成真正模型"""
    return {
        "color": random.choice(color_labels),
        "pattern": random.choice(pattern_labels),
        "category": random.choice(category_labels),
        "gender": gender,
    }
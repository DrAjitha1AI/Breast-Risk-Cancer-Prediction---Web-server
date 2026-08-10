import pickle
from pathlib import Path

import pandas as pd


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "cancerpredict_finalmodel.sav"


# Load model once when application starts
with open(MODEL_PATH, "rb") as model_file:
    loaded_model = pickle.load(model_file)


# IMPORTANT:
# Keep this order exactly the same as the model training data.
FEATURE_COLUMNS = [
    "Family_History",
    "BMI",
    "High_Fat_Diet",
    "Smoking",
    "Alcohol",
    "HRT_Usage",
    "Late_Menopause",
    "No_or_Late_Pregnancy",
    "Breastfed",
    "Estrogen_Cosmetics"
]


def predict_risk(user_data):
    """
    Predict breast cancer risk level.

    Returns:
        int:
            0 = Low
            1 = Moderate
            2 = High
    """

    data = pd.DataFrame(
        [[
            user_data["Family_History"],
            user_data["BMI"],
            user_data["High_Fat_Diet"],
            user_data["Smoking"],
            user_data["Alcohol"],
            user_data["HRT_Usage"],
            user_data["Late_Menopause"],
            user_data["No_or_Late_Pregnancy"],
            user_data["Breastfed"],
            user_data["Estrogen_Cosmetics"]
        ]],
        columns=FEATURE_COLUMNS
    )

    prediction = loaded_model.predict(data)[0]

    return int(prediction)
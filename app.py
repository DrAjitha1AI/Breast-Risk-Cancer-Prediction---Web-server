from flask import Flask, render_template, request
from src.predict import predict_risk


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get form values
        family_history = int(request.form["Family_History"])
        bmi = float(request.form["BMI"])
        high_fat_diet = int(request.form["High_Fat_Diet"])
        smoking = int(request.form["Smoking"])
        alcohol = int(request.form["Alcohol"])
        hrt_usage = int(request.form["HRT_Usage"])
        late_menopause = int(request.form["Late_Menopause"])
        no_or_late_pregnancy = int(
            request.form["No_or_Late_Pregnancy"]
        )
        breastfed = int(request.form["Breastfed"])
        estrogen_cosmetics = int(
            request.form["Estrogen_Cosmetics"]
        )

        # Store inputs
        user_data = {
            "Family_History": family_history,
            "BMI": bmi,
            "High_Fat_Diet": high_fat_diet,
            "Smoking": smoking,
            "Alcohol": alcohol,
            "HRT_Usage": hrt_usage,
            "Late_Menopause": late_menopause,
            "No_or_Late_Pregnancy": no_or_late_pregnancy,
            "Breastfed": breastfed,
            "Estrogen_Cosmetics": estrogen_cosmetics
        }

        # Prediction
        prediction = predict_risk(user_data)

        # Risk information
        risk_map = {
            0: {
                "level": "Low",
                "class": "low",
                "icon": "✓",
                "message": (
                    "The model classified the provided "
                    "information as a low-risk category."
                )
            },
            1: {
                "level": "Moderate",
                "class": "moderate",
                "icon": "!",
                "message": (
                    "The model classified the provided "
                    "information as a moderate-risk category."
                )
            },
            2: {
                "level": "High",
                "class": "high",
                "icon": "!",
                "message": (
                    "The model classified the provided "
                    "information as a high-risk category."
                )
            }
        }

        risk = risk_map.get(
            prediction,
            {
                "level": "Unknown",
                "class": "unknown",
                "icon": "?",
                "message": "Unable to determine the risk category."
            }
        )

        return render_template(
            "result.html",
            prediction=prediction,
            risk=risk,
            user_data=user_data
        )

    except (ValueError, KeyError, TypeError):
        return render_template(
            "result.html",
            prediction=None,
            risk={
                "level": "Input Error",
                "class": "error",
                "icon": "!",
                "message": (
                    "Please check all entered values and "
                    "submit the form again."
                )
            },
            user_data={}
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
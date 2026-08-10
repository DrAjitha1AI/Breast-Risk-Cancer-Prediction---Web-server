# Breast Cancer Risk Prediction

## Machine Learning-Based Breast Cancer Risk Assessment Web Application

This project is a Flask-based web application that uses a trained machine learning model to classify breast cancer risk into three categories:

- Low Risk
- Moderate Risk
- High Risk

The application is designed as an educational and research-oriented machine learning project demonstrating the integration of a trained classification model with a professional web interface.

---

## Project Objectives

The objectives of this project are to:

- Apply machine learning to breast cancer risk classification.
- Provide a simple web-based risk assessment interface.
- Demonstrate deployment of a machine learning model using Flask.
- Create a responsive medical research-oriented user interface.
- Deploy the application using Render.

---

## Input Variables

The model uses the following variables:

1. Family History of Breast Cancer
2. Body Mass Index (BMI)
3. High Fat Diet
4. Current Smoking
5. Frequent Alcohol Consumption
6. Hormonal Replacement Therapy Usage
7. Late Menopause
8. Late or No Pregnancy
9. Breastfeeding
10. Estrogen-Based Cosmetics Usage

---

## Risk Categories

The model output is mapped as:

| Model Output | Risk Level |
|--------------|------------|
| 0 | Low |
| 1 | Moderate |
| 2 | High |

---

## Technology Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML5
- CSS3
- JavaScript
- Gunicorn
- Render

---

## Project Structure

```text
Breast Risk Cancer Prediction - Web server/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── cancerpredict_rfmodel.sav
│
├── src/
│   ├── __init__.py
│   └── predict.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── breast-cancer-ribbon.svg
│
└── notebooks/
    └── Breast_Cancer_risk_final_model.ipynb
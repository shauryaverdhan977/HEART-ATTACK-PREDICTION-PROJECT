from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
import os

app = Flask(__name__)

# ===== YOUR ORIGINAL CODE (slightly adjusted) =====

# Load dataset
csv_path = os.path.join(os.path.dirname(__file__), 'Medicaldataset.csv')
data = pd.read_csv(csv_path)

# Convert Result column
data['Result'] = data['Result'].map({'negative':0, 'positive':1})

# Features and target
X = data[['Age','Gender','Heart rate','Systolic blood pressure',
          'Diastolic blood pressure','Blood sugar']]
y = data['Result']

# Train model
model = LogisticRegression()
model.fit(X, y)

# ===== NEW WEB PART STARTS HERE =====

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get data from form
    age = float(request.form["age"])
    gender = float(request.form["gender"])
    hr = float(request.form["hr"])
    sys_bp = float(request.form["sys_bp"])
    dia_bp = float(request.form["dia_bp"])
    sugar = float(request.form["sugar"])

    # Create dataframe (same as your new_patient)
    new_patient = pd.DataFrame({
        'Age':[age],
        'Gender':[gender],
        'Heart rate':[hr],
        'Systolic blood pressure':[sys_bp],
        'Diastolic blood pressure':[dia_bp],
        'Blood sugar':[sugar]
    })

    # Prediction (same as your logic)
    prediction = model.predict(new_patient)[0]
    probability = model.predict_proba(new_patient)[0][1]

    result = "Positive (Risk)" if prediction == 1 else "Negative (Safe)"

    return render_template("index.html", result=result, prob=round(probability,2))


# Run server
if __name__ == "__main__":
    app.run(debug=True)
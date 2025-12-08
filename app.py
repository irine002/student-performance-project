from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and train model once at start
data = pd.read_csv("data/student_data.csv")
X = data[['study_hours', 'attendance', 'previous_score']]
y = data['passed']

model = LogisticRegression()
model.fit(X, y)

@app.route('/')
def home():
    return """
    <h2>Student Performance Predictor</h2>
    <form method="post" action="/predict">
        Study Hours: <input type="number" name="study_hours"><br><br>
        Attendance (%): <input type="number" name="attendance"><br><br>
        Previous Score: <input type="number" name="previous_score"><br><br>
        <button type="submit">Predict</button>
    </form>
    """

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['study_hours'])
    attendance = float(request.form['attendance'])
    previous_score = float(request.form['previous_score'])

    prediction = model.predict([[study_hours, attendance, previous_score]])

    result = "✅ PASS" if prediction[0] == 1 else "❌ FAIL"

    return f"<h2>Prediction Result: {result}</h2><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)

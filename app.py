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
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        previous_score = float(request.form['previous_score'])

        # Predict
        prediction = model.predict([[study_hours, attendance, previous_score]])
        result = "✅ PASS" if prediction[0] == 1 else "❌ FAIL"
        
        return render_template('index.html', prediction_text=f"Prediction: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

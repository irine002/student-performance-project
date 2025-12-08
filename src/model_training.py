import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv("data/student_data.csv")

# Features (X) and Target (y)
X = data[['study_hours', 'attendance', 'previous_score']]
y = data['passed']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Show accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Test manual prediction
sample_data = [[7, 80, 70]]
prediction = model.predict(sample_data)
print("Prediction for student (7 hrs, 80% attendance, score 70):", prediction[0])

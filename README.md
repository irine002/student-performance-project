Student Performance Prediction Web App
📝 Project Description

This is an end-to-end Data Science project built using Python and Flask.
It predicts whether a student will pass or fail based on their:

Study hours

Attendance percentage

Previous scores

The project demonstrates:

Data Cleaning & Preprocessing

Exploratory Data Analysis (EDA)

Machine Learning model training (Logistic Regression)

Deployment as a web application

💻 Features

Clean and structured Python project

Interactive web interface for predictions

Easy to run locally

Professional folder structure for job portfolios

🗂 Folder Structure
student-performance-project/
│
├── data/
│   └── student_data.csv      # Sample dataset
├── notebooks/                # Optional for EDA
├── src/
│   ├── data_preprocessing.py # Load and clean data
│   └── model_training.py     # Train ML model & EDA
├── app.py                     # Flask web app
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

⚙️ Technologies Used

Python 3.x

Pandas & NumPy

Matplotlib & Seaborn

Scikit-learn

Flask

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/irine002/student-performance-project.git
cd student-performance-project

2️⃣ Install dependencies
pip install -r requirements.txt
pip install flask matplotlib seaborn scikit-learn pandas

3️⃣ Run the web app
python app.py


Open your browser at:

http://127.0.0.1:5000/

![alt text](<Screenshot 2025-12-08 174200.png>)

📈 Model Details

Algorithm: Logistic Regression

Features used: study_hours, attendance, previous_score

Target: passed (1 = Pass, 0 = Fail)

Model accuracy: ~50% (dataset is small, but pipeline is fully functional)

💡 Next Steps / Improvements

Add more student data to improve model accuracy

Deploy online using Heroku or Render

Add more features like assignments, extracurriculars, and test scores

📂 Author

Name: Irine

Email: irinevincent932@gmail.com

GitHub: irine002
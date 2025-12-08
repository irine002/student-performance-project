import pandas as pd

def load_and_clean_data():
    # Load the dataset
    data = pd.read_csv("data/student_data.csv")

    # Check missing values
    print("Missing values before cleaning:")
    print(data.isnull().sum())

    # Fill missing numeric values with the mean
    data.fillna(data.mean(), inplace=True)

    print("\nMissing values after cleaning:")
    print(data.isnull().sum())

    return data

if __name__ == "__main__":
    df = load_and_clean_data()
    print("\nCleaned Data:")
    print(df)

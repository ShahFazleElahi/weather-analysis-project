import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])  # Convert Date to datetime
    return df

def preprocess_data(df):
    """Preprocess data (e.g., fill missing values)."""
    df.fillna(0, inplace=True)  # Fill any missing values
    return df

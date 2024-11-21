import pandas as pd

def load_and_process_data():
    """
    Loads the dataset and performs basic preprocessing (e.g., handling missing values).
    Returns the processed DataFrame.
    """
    df = pd.read_csv('data/raw/data.csv')
    
    df.fillna(df.mean(), inplace=True)
    return df

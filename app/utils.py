import pandas as pd

def load_data(country):
    file_path = f"data/{country.lower()}_clean.csv"
    try:
        df = pd.read_csv(file_path)
        df["Country"] = country  
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file for {country} not found at {file_path}")
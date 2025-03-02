# db.py
import pandas as pd

def load_data(csv_file='netflix_titles.csv'):
    """
    Load Netflix CSV data into a pandas DataFrame.
    """
    df = pd.DataFrame()
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found. Ensure it is in the same directory.")
    except Exception as e:
        print("An error occurred while loading the CSV file:", e)
    return df

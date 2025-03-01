import sqlite3
import os
import pandas as pd

DB_NAME = "movies.db"

def create_database():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                            show_id TEXT PRIMARY KEY,
                            title TEXT,
                            director TEXT,
                            cast TEXT,
                            country TEXT,
                            date_added TEXT,
                            release_year INTEGER,
                            rating TEXT,
                            duration TEXT,
                            listed_in TEXT,
                            description TEXT)''')
        conn.commit()
        conn.close()
        print("✅ Database initialized successfully.")
    except Exception as e:
        print(f"❌ Error creating database: {e}")

def insert_data_from_csv(csv_path):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        data = pd.read_csv(csv_path)
        data.fillna("Unknown", inplace=True)
        for _, row in data.iterrows():
            cursor.execute("""
                INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(row))
        conn.commit()
        conn.close()
        print("✅ Data inserted successfully.")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")

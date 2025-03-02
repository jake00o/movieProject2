# ui.py
import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style
from pyfiglet import figlet_format

def clear_screen():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass

def fancy_heading(text):
    try:
        heading = figlet_format(text, font="standard")
        print(Fore.CYAN + heading + Style.RESET_ALL)
    except:
        print(text)

def goodbye_animation():
    # Convert "Goodbye..." into ASCII art
    ascii_goodbye = figlet_format("Goodbye...", font="standard")
    # Split the ASCII art into lines
    lines = ascii_goodbye.split("\n")

    # Print line by line, char by char
    for line in lines:
        for char in line:
            print(Fore.GREEN + char, end='', flush=True)
            time.sleep(0.005)  
        print()  # Go to the next line
    
    print(Style.RESET_ALL)
    time.sleep(0.5) 
def show_common_genres(df):
    """
    Display a bar chart of the top 5 genres found in the dataset.
    """
    try:
        clear_screen()
        fancy_heading("Most Common Genres")

        # Split 'listed_in'
        genres_series = df['listed_in'].dropna().str.split(', ')
        all_genres = []
        for g_list in genres_series:
            all_genres.extend(g_list)

        # Count frequencies
        freq_dict = {}
        for g in all_genres:
            freq_dict[g] = freq_dict.get(g, 0) + 1

        # Sort and take top 5
        sorted_genres = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        top_5 = sorted_genres[:5]

        print(Fore.YELLOW + "Top 5 Genres (Count)" + Style.RESET_ALL)
        for (genre, count) in top_5:
            print(f"{genre} => {count}")

        # Plot
        labels, counts = zip(*top_5)
        plt.figure()
        plt.bar(labels, counts)
        plt.title("Top 5 Genres on Netflix")
        plt.xlabel("Genre")
        plt.ylabel("Frequency")
        # Annotate each bar
        for i, v in enumerate(counts):
            plt.text(i, v + 0.5, str(v), ha='center')
        plt.show()

        input("\nPress Enter to return to the menu...")
    except Exception as e:
        print("Error in show_common_genres:", e)
        input("Press Enter to continue...")

def show_ratings_distribution(df):
    """
    Display a bar chart for distribution by rating.
    """
    try:
        clear_screen()
        fancy_heading("Distribution by Rating")

        rating_counts = df['rating'].value_counts()
        print(Fore.YELLOW + "Rating Counts (Top 10):" + Style.RESET_ALL)
        print(rating_counts.head(10))

        plt.figure()
        plt.bar(rating_counts.index, rating_counts.values)
        plt.title("Rating Distribution")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        # Annotate
        for i, val in enumerate(rating_counts.values):
            plt.text(i, val + 0.5, str(val), ha='center')
        plt.show()

        input("\nPress Enter to return to the menu...")
    except Exception as e:
        print("Error in show_ratings_distribution:", e)
        input("Press Enter to continue...")

def show_year_wise_additions(df):
    """
    Display how many titles were added each year, as a line chart.
    """
    try:
        clear_screen()
        fancy_heading("Yearly Content Additions")

        # Convert date_added to datetime
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df['year_added'] = df['date_added'].dt.year

        year_counts = df['year_added'].value_counts().dropna().sort_index()
        print(Fore.YELLOW + "Additions By Year:" + Style.RESET_ALL)
        print(year_counts)

        plt.figure()
        plt.plot(year_counts.index, year_counts.values, marker='o')
        plt.title("Trend of Content Additions Over the Years")
        plt.xlabel("Year")
        plt.ylabel("Number of Additions")

        for x, y in zip(year_counts.index, year_counts.values):
            plt.text(x, y + 5, str(int(y)), ha='center')

        plt.show()

        input("\nPress Enter to return to the menu...")
    except Exception as e:
        print("Error in show_year_wise_additions:", e)
        input("Press Enter to continue...")


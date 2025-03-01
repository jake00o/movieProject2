import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore, Style
from pyfiglet import figlet_format

class MovieDatabase:
    def __init__(self, file_path):
        try:
            self.file_path = file_path
            self.data = pd.read_csv(file_path)
            if self.data.empty:
                raise ValueError("Dataset is empty or could not be loaded correctly.")
            print(Fore.GREEN + "✅ Dataset loaded successfully!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"❌ Error loading dataset: {e}" + Style.RESET_ALL)
            self.data = None

    def get_most_common_genres(self, top_n=5):
        if self.data is None:
            print(Fore.RED + "❌ Error: Dataset is not loaded correctly." + Style.RESET_ALL)
            return None
        try:
            self.data['listed_in'] = self.data['listed_in'].str.split(', ')
            all_genres = [genre for sublist in self.data['listed_in'].dropna() for genre in sublist]
            genre_counts = pd.Series(all_genres).value_counts()
            self._plot_bar_chart(genre_counts.head(top_n), "Most Common Genres", "Genres", "Count")
            return genre_counts.head(top_n)
        except Exception as e:
            print(Fore.RED + f"❌ Error analyzing genres: {e}" + Style.RESET_ALL)
            return None

    def get_content_distribution_by_rating(self):
        if self.data is None:
            print(Fore.RED + "❌ Error: Dataset is not loaded correctly." + Style.RESET_ALL)
            return None
        try:
            rating_counts = self.data['rating'].value_counts()
            self._plot_bar_chart(rating_counts, "Content Distribution by Rating", "Ratings", "Count")
            return rating_counts
        except Exception as e:
            print(Fore.RED + f"❌ Error analyzing content distribution by rating: {e}" + Style.RESET_ALL)
            return None

    def get_addition_trend_over_years(self):
        if self.data is None:
            print(Fore.RED + "❌ Error: Dataset is not loaded correctly." + Style.RESET_ALL)
            return None
        try:
            if 'date_added' not in self.data.columns:
                print(Fore.RED + "❌ Error: 'date_added' column is missing." + Style.RESET_ALL)
                return None
            self.data['date_added'] = pd.to_datetime(self.data['date_added'], errors='coerce')
            self.data.dropna(subset=['date_added'], inplace=True)
            year_counts = self.data['date_added'].dt.year.value_counts().sort_index()
            self._plot_line_chart(year_counts, "Trend of Additions Over the Years", "Year", "Number of Additions")
            return year_counts
        except Exception as e:
            print(Fore.RED + f"❌ Error analyzing additions over years: {e}" + Style.RESET_ALL)
            return None

    def display_heading(self, text):
        print(Fore.CYAN + figlet_format(text) + Style.RESET_ALL)

    def _plot_bar_chart(self, data, title, xlabel, ylabel):
        plt.figure(figsize=(12, 6))
        sns.barplot(x=data.index, y=data.values, palette="coolwarm")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.show()

    def _plot_line_chart(self, data, title, xlabel, ylabel):
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data.values, marker='o', linestyle='-', color='b')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

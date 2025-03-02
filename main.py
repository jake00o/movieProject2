"""
main.py - CLI entry point for it
This module handles user interaction and menu logic.
"""

import time
from colorama import init, Fore, Style
from db import load_data
from ui import (
    clear_screen,
    fancy_heading,
    goodbye_animation,
    show_common_genres,
    show_ratings_distribution,
    show_year_wise_additions
)

def main():
    init(autoreset=True)

    # Load CSV
    df = load_data('netflix_titles.csv')
    if df.empty:
        print(Fore.RED + "No data found or file missing. Exiting..." + Style.RESET_ALL)
        time.sleep(2)
        return

    while True:
        try:
            clear_screen()
            fancy_heading(" MOVIES APPLICATION")

            print(Fore.YELLOW + "1." + Style.RESET_ALL + " Show Most Common Genres")
            print(Fore.YELLOW + "2." + Style.RESET_ALL + " Show Distribution by Rating")
            print(Fore.YELLOW + "3." + Style.RESET_ALL + " Show Trend of Additions Over the Years")
            print(Fore.YELLOW + "4." + Style.RESET_ALL + " Exit")

            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == '1':
                show_common_genres(df)
            elif choice == '2':
                show_ratings_distribution(df)
            elif choice == '3':
                show_year_wise_additions(df)
            elif choice == '4':
                clear_screen()
                goodbye_animation()
                break
            else:
                print(Fore.RED + "Invalid choice! Please try again." + Style.RESET_ALL)
                time.sleep(1)
        except Exception as e:
            print(Fore.RED + f"Error in main loop: {e}" + Style.RESET_ALL)
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"Fatal error: {e}" + Style.RESET_ALL)
        time.sleep(2)

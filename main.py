import time
from objects import MovieDatabase
from db import create_database, insert_data_from_csv
from ui import print_menu, goodbye_animation

def main():
    dataset_path = "netflix_titles.csv"
    create_database()
    insert_data_from_csv(dataset_path)
    movie_db = MovieDatabase(dataset_path)

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Most Common Genres:")
            print(movie_db.get_most_common_genres())
        elif choice == "2":
            print("Content Distribution by Rating:")
            print(movie_db.get_content_distribution_by_rating())
        elif choice == "3":
            print("Addition Trend Over Years:")
            print(movie_db.get_addition_trend_over_years())
        elif choice == "4":
            goodbye_animation()
            break
        else:
            print("❌ Invalid choice, please try again.")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()

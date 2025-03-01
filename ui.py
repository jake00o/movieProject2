import os
import time
from pyfiglet import figlet_format

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print(figlet_format("Movie DB"))
    print("1. View Most Common Genres")
    print("2. View Content Distribution by Rating")
    print("3. View Addition Trend Over Years")
    print("4. Exit")

def goodbye_animation():
    message = "Goodbye!"
    clear_screen()
    print("\n")
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.2)
    print("\n")
    time.sleep(1)

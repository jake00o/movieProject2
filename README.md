# Netflix Movies CLI Application

## Overview
This is a command-line application that analyzes Netflix Movies & TV Shows data using Python. The program provides:

- Data insights into genres, ratings, and trends.
- Interactive visualizations using Matplotlib & Seaborn.
- Database storage using SQLite.
- Menu-driven interface with PyFiglet and Colorama for styling.

## Features
- **Data Analysis**: Uses Pandas & NumPy for efficient data processing.
- **Visualizations**: Displays bar charts and line graphs using Matplotlib & Seaborn.
- **Database Storage**: Stores Netflix data in SQLite for easy retrieval.
- **User Interface**: Menu-driven CLI with a colorful UI using PyFiglet and Colorama.

## Setup Instructions
### 1. Clone the Repository from GitHub
```sh
git clone https://github.com/jake00o/movieproject2
cd movieproject2
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```

### 3. Activate Virtual Environment
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 4. Install Dependencies
```sh
pip install pandas numpy matplotlib colorama pyfiglet
```

### 5. Run the Program
```sh
python main.py
```

## File Descriptions
- `objects.py` - Objects that Handles data analysis and visualization.
- `db.py` - Manages database operations.
- `ui.py` - Manages the user interface, including animations.
- `main.py` - Integrates all components and runs the program.

## Data Analysis Implemented
1. **Most Common Genres** - Displays a bar chart of the most frequent Netflix genres.
2. **Content Distribution by Rating** - Shows how content is distributed across different ratings.
3. **Trend of Additions Over the Years** - Visualizes the trend of movie & TV show additions over time.

## References
- Dataset: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

## Additional Notes
- Ensure you have **Python 3.7+** installed.
- Run the program **inside the virtual environment** to avoid dependency issues.
- The application is **terminal-based** and displays **visual charts** for insights.



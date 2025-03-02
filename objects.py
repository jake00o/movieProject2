# objects.py
import pandas as pd

class NetflixItem:
    def __init__(
        self, show_id, title, director, cast, country, date_added,
        release_year, rating, duration, listed_in, description
    ):
        self.show_id = show_id
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description

def create_items_from_df(df: pd.DataFrame):
    items = []
    try:
        for _, row in df.iterrows():
            item = NetflixItem(
                show_id=row.get('show_id', ''),
                title=row.get('title', ''),
                director=row.get('director', ''),
                cast=row.get('cast', ''),
                country=row.get('country', ''),
                date_added=row.get('date_added', ''),
                release_year=row.get('release_year', ''),
                rating=row.get('rating', ''),
                duration=row.get('duration', ''),
                listed_in=row.get('listed_in', ''),
                description=row.get('description', '')
            )
            items.append(item)
    except Exception as e:
        print("Error creating NetflixItem objects:", e)
    return items

import re
from src.file_helper import read_data
from src.components.dict_handler import set_data_title_release_date_genres
from src.components.filters_string import get_genre


# List all movies which title starts with T followed by any characters and have genre Animation
def feature_3(title, genre):
    result = []
    movies = read_data('movies', 'csv')
    for movie in movies:
        data = set_data_title_release_date_genres(movie)
        genres = data['genres']
        if title == data['title'][0] and genre in genres:
            data['genres'] = get_genre(genre, genres)
            result.append(data)
    return result

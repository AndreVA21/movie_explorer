from src.file_helper import read_data
from src.components.filters_string import *
from src.components.dict_handler import set_data_title_release_date_genres

def feature_4(title):
    result = []
    movies = read_data('movies')
    for movie in movies:
        data = set_data_title_release_date_genres(movie)
        if title == data['title']:
            result.append(data)
    return result
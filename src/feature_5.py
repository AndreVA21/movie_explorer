from src.file_helper import read_data
from src.components.dict_handler import set_data_title_release_date_genres, result_tag_format
from src.components.filters_string import *


def feature_5(title,tag):

    data = []
    if tag == "all":
        movies = read_data('movies','csv')
        tags = read_data('tags','csv')

        for movie in movies:
            result = set_data_title_release_date_genres(movie)
            if title == result['title']:  
                result['tags'] = [result_tag_format(tag) for tag in tags if movie['movieId'] == tag['movieId']]
                data.append(result)
    return data


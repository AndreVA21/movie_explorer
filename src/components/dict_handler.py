from src.components.filters_string import *
from src.file_helper import read_data


def get_dictionary() -> dict:
    data = []
    csvReader = read_data('movies')

    for rows in csvReader:
        data.append(set_data_title_release_date_genres(rows))
    return data


def get_dictionary_6(value):
    data, filter_rating = [], []
    csvReader = read_data('movies')
    csvraiting = read_data('ratings')

    for rows in csvraiting:
        if rows['rating'] == value:
            filter_rating.append(rows)

    for rows in csvReader:
        for rating in filter_rating:
            if rows['movieId'] == rating['movieId']:
                data.append(set_movie_data(rows, rating))
    return data


def set_data_title_release_date_genres(rows) -> dict:
    dummy_title = helper_find(rows['title'])
    return {
        'title': normalized(delate_string(dummy_title, rows['title'])[:-1]),
        'release_date': filter_handler(dummy_title),
        'genres': genres_handler(rows['genres'])
    }


def result_tag_format(tag):
    result = {}
    result['tag'] = tag['tag']
    result['date_time'] = convert_epoch_to_datetime_string(tag['timestamp'])
    return result


def set_movie_data(rows, rows_rating) -> dict:
    dummy_title = helper_find(rows['title'])
    return {
        'title': normalized(delate_string(dummy_title, rows['title'])[:-1]),
        'release_date': filter_handler(dummy_title),
        'genres': genres_handler(rows['genres']),
        'timestamp': convert_epoch_to_datetime_string(rows_rating['timestamp']),
        'rating': float(rows_rating['rating'])
    }

import re
from src.file_helper import read_data


def get_genre(genre, genres):
    return [g for g in genres if g == genre]


def get_release_date(title):
    if '(' not in title and ')' not in title:
        return ""
    return int(re.findall(r'-?\d+\.?\d*', title)[-1])


def get_format_feature_3(movie):
    result = {}
    title = movie['title']
    result['title'] = title.split(f" ({get_release_date(title)})")[0]
    result['release_date'] = get_release_date(title)
    genres = str(movie['genres']).split('|')
    result['genres'] = genres
    return result


#List all movies which title starts with T followed by any characters and have genre Animation
def feature_3(title, genre):
    result = []
    movies = read_data('movies','csv')
    for movie in movies:
        data = get_format_feature_3(movie)
        genres = data['genres']
        if title == data['title'][0] and genre in genres:
            data['genres'] = get_genre(genre, genres)
            result.append(data)
    return result
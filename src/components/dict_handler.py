from src.components.filters_string import *
from src.file_helper import read_data

def get_dictionary() -> dict:
    
    data = []
    csvReader= read_data('movies')

    for rows in csvReader:
        data.append(set_data_title_release_date_genres(rows))
    
    return data

def get_dictionary_6(value):
    data = []
    csvReader= read_data('movies')
    csvraiting = read_data('ratings')

    for rows in csvReader:
        for raiting_rows in csvraiting:
            if rows['movieId'] == raiting_rows['movieId'] and raiting_rows['rating'] == value:
                data.append(set_movie_data(rows, raiting_rows))

    return data
    
def set_data_title_release_date_genres(rows) -> dict:
    return {'title':normalized(delate_string(helper_find(rows['title']), rows['title'])[:-1]),
    'release_date':filter_handler(helper_find(rows['title'])),
    'genres':genres_handler(rows['genres'])}



def set_movie_data(rows, rows_rating) -> dict:
    return {
        'movieId':rows['movieId'],
        'title':normalized(
            delate_string(
                helper_find(rows['title']), rows['title']
                )[:-1]),
        'release_date':filter_handler(helper_find(rows['title'])),
        'genres':genres_handler(rows['genres']),
        'timestamp':rows_rating['timestamp'],
        'rating':float(rows_rating['rating'])
    }
###filters###
    
if __name__ == '__main__':
    print(get_dictionary())
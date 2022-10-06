from src.components.filters_string import *
from file_helper import read_data

def get_dictionary() -> dict:
    
    data = []
    csvReader= read_data('movies')

    for rows in csvReader:
        data.append(set_data_title_release_date_genres(rows))
    
    return data

def set_data_title_release_date_genres(rows) -> dict:
    return {'title':normalized(delate_string(helper_find(rows['title']), rows['title'])[:-1]),
    'release_date':filter_handler(helper_find(rows['title'])),
    'genres':genres_handler(rows['genres'])}

###filters###
    
if __name__ == '__main__':
    print(get_dictionary())
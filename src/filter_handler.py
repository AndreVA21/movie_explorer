from components.filters_string import *
from file_helper import read_data

def get_dictionary() -> dict:
    
    data = []
    
    csvReader= read_data('movies')

    for rows in csvReader:
        data.append(
            {'title':normalized(delate_string(helper_find(rows['title']), rows['title'])[:-1]),
            'release_date':filter_handler(helper_find(rows['title'])),
            'genres':genres_handler(rows['genres'])}
        )
    
    return data

def filter_by_all_title_decen_acend(acendent) -> dict:

    data_json = get_dictionary()
    sorted_dict = sorted(data_json, key=lambda x: x["title"],reverse=acendent)
    return sorted_dict


print(filter_by_all_title_decen_acend(False))
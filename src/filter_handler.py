from components.filters_string import *
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
    
def filter_by_all_title_decen_acend(order, order_by) -> dict:

    data_json = get_dictionary()
    reve = False if order=='asc' or 'ascendent' else True

    sorted_dict = sorted(data_json, key=lambda x: x[order_by],reverse=reve)
    return sorted_dict

def filter_list_all_movies_with_rating_of_3():
    return 0

if __name__ == '__main__':
    print(filter_by_all_title_decen_acend('asc','title'))
from src.components.dict_handler import *

def filter_by_all_title_decen_acend(order, order_by) -> dict:

    data_json = get_dictionary()
    reve = False if order=='asc' or 'ascendent' else True

    sorted_dict = sorted(data_json, key=lambda x: x[order_by],reverse=reve)
    return sorted_dict

def filter_list_all_movies_with_rating_of_3():
    return 0
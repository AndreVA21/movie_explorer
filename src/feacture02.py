from src.components.dict_handler import *

def filter_by_all_title_decen_acend(order, order_by) -> dict:

    data_json = get_dictionary()
    reve = False if order=='asc' or order == 'ascendent' else True
    sorted_dict = sorted(data_json, key=lambda x: x[order_by],reverse=reve)

    return sorted_dict

if __name__ == '__main__':
    print(filter_by_all_title_decen_acend('asc','release_date'))

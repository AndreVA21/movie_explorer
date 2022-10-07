from src.components.dict_handler import *


def feature_2(order, order_by) -> dict:
    data_json = get_dictionary()
    reve = False if order == 'asc' or order == 'ascendent' else True
    sorted_dict = sorted(data_json, key=lambda x: x[order_by], reverse=reve)
    return sorted_dict

from src.components.filters_string import *

def test_filter_handler():
    sltring_list = ['find 120 number']
    date = filter_handler(sltring_list)

    assert date is 120

def test_filter_handler_empty():
    sltring_list = 'no numbers in the string'
    date = filter_handler(sltring_list)

    assert date is 0

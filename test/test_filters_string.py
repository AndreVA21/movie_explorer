from src.components.filters_string import *

def test_filter_handler():
    sltring_list = 'find 120 number'
    date = filter_handler(sltring_list)

    assert date is 120

def test_filter_handler_empty():
    sltring_list = 'no numbers in the string'
    date = filter_handler(sltring_list)

    assert date is 0

def test_helper_find():
    list_string = 'string find (find in parenthesis)'
    date = helper_find(list_string)

    assert date is 'find in parenthesis'

def test_genres_handler():
    genders = 'action|comedy|funny'
    date = genres_handler(genders)

    assert date is ['action','comedy','funny']

def test_delate_string():
    list_remove = ['do not del','del this']
    string = 'do not del that string just del this'
    date = delate_string(list_remove, string)

    assert date is 'do not del that string just'

def test_normalized():
    string = 'á and é'
    date = test_normalized(string)

    assert date is 'a and e'
import re

def filter_handler(sltring_list) -> int:
    year=[]
    for element in sltring_list:
        year=[abs(int(s)) for s in re.findall(r'-?\d+\.?\d*', element)]
    return 0 if year==[] else year[0]

def helper_find(String) ->list:
    return re.findall(r'[(](.*?)[)]', String) 

def genres_handler(string) ->list:
    return string.split('|')

def delate_string(list_remove,string):
    if list_remove ==[]:
        return 'None'
    else:
        str_list = string.split('('+list_remove[-1]+')')
        return "".join(str_list)

def normalized(string):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        string = string.replace(a, b).replace(a.upper(), b.upper())
    return string
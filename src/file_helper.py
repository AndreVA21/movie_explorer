import json
from csv import DictReader

PATH_FILES = '/Users/miguelgemio/Jala/Python-Backend/Assignements/final_assig/movie_explorer/data/'


def read_data(file_name, extension='csv'):
    path, data = (PATH_FILES + file_name + '.' + extension), []  # We get the path of the file.
    try:
        with open(path, 'r') as file:
            if extension.lower() == 'csv': 
                data = list(DictReader(file))   # Convert csv data to a list of Dictionaries
            elif extension.lower() == 'json':
                data.append(json.load(file))  # Convert json data to a list of Dictionaries
    except Exception as e:
        print(f'File not Found in path: {path}.\n', e)
    finally:
        return data  # Returns a List of Dictionaries 

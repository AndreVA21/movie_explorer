from numpy import delete
from src.file_helper import read_data
from datetime import datetime
from src.components.filters_string import helper_find, delate_string


def convert_epoch_to_datetime_string(timestamp):
    date_time = datetime.fromtimestamp(float(timestamp))
    day = date_time.strftime('%A')
    month = date_time.strftime('%B')
    time = str(date_time.strftime('%I:%M:%S %p'))
    time = time[1:] if time.startswith('0') else time
    new_date = day + ', ' + month + ' ' + str(date_time.month) \
        + ', ' + str(date_time.year) + ' ' + time
    return new_date


def get_output_format(output=[]):
    new_output = []
    for element in output:
        data = {}
        genres = element.get('genres').split('|')
        str_date = convert_epoch_to_datetime_string(element.get('timestamp'))
        data['title'] = delate_string(helper_find(element['title']), element['title'])[:-1]
        data['release_date'] = helper_find(element['title'])[-1]
        data['genres'] = genres
        data['ratings'] = [{
            'date_time': str_date, 
            'rating': element.get('rating')
        }]
        new_output.append(data)
    return new_output


def feature_8(request = {}):
    output = []
    if request.get('rating') == 'all':
        ratings_data = read_data('ratings', 'csv')
        movies_data = read_data('movies', 'csv')

        for element in ratings_data:
            if element.get('userId') == str(request.get('user')):
                output.append(element)
        movies_ids = [element.get('movieId') for element in output]
        filter_movies_data = []
        
        for element in movies_data:
            if element.get('movieId') in movies_ids:
                filter_movies_data.append(element)

        for element in output:
            for movie in filter_movies_data:
                if element.get('movieId') == movie.get('movieId'):
                    element['title'] = movie.get('title')
                    element['genres'] = movie.get('genres')
                    element.pop('userId')
                    element.pop('movieId')
                    
        output = get_output_format(output)
    else:
        print('For feature 8, the "-r|--rating" only could be "all"')
    return output

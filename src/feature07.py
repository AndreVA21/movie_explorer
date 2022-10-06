from src.file_helper import read_data

def feature7(res):
    movies = read_data('movies')
    data = []
    
    if res.get('genre') == 'all':
        for movie in movies:
            genres = str(movie['genres']).split('|')
            [data.append(genre) for genre in genres if genre not in data]
       
         
    return data
    

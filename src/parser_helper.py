import argparse
import sys

def create_new_parser():
    parser = argparse.ArgumentParser(description='Movies Explorer App,'
                                     'explore the Movies, Raitings y tags.')
    parser.add_argument('-t', '--title', type=str, help='Title of a movie. (a, avengers)',
                        default=None, required=False)
    parser.add_argument('-o', '--order', type=str, help='Order to show the results. (asc|desc).',
                        default=None, required=False,
                        choices=['asc', 'desc', 'ascendent', 'descendent'])
    parser.add_argument('-b', '--by', type=str, help='property on which it is sorted.',
                        choices=['title', 'release_date', 'count'],
                        default=None, required=False)
    parser.add_argument('-g', '--genre', type=str, help='Genre of the movies. (Animation)',
                        default=None, required=False)
    parser.add_argument('-rd', '--release_date', type=str,
                        help='Release date of the movies. (1954)',
                        choices=['all'], default=None, required=False)
    parser.add_argument('-tg', '--tag', type=str, help='Tags  of the movies. (Tom Cruise)',
                        choices=['all'], default=None, required=False)
    parser.add_argument('-r', '--rating', type=str, help='Rating of the movies. (3.0)',
                        default=None, required=False)
    parser.add_argument('-u', '--user', type=int, help="User's id. (1234)",
                        default=None, required=False)

    args = parser.parse_args()
    str_args = ' '.join(sys.argv)
    
    if args.title or args.order or args.by or args.genre or args.release_date or args.tag or\
        args.rating or args.user:
        request = {
            'title': args.title,
            'order': args.order,
            'order_by': args.by,
            'genre': args.genre,
            'release_date': args.release_date,
            'tag': args.tag,
            'rating': args.rating,
            'user': args.user,
        }
    else:
        request = {}
    return request, str_args


def get_keys_not_none_arguments(request):
    return [key for key, value in request.items() if value != None] 


def is_feature_2(request={}):
    # List all movies sorted by --by.
    expected_keys = ['title', 'order', 'order_by']
    key_arguments = get_keys_not_none_arguments(request)
    if request.get('title') and len(request.get('title')) > 1 and expected_keys == key_arguments:
        return True


def is_feature_3(request={}):
    # List movies by genere and the title starts with 'x' character.
    expected_keys = ['title', 'genre']
    key_arguments = get_keys_not_none_arguments(request)
    if request.get('title') and expected_keys == key_arguments:
        if len(request.get('title')) == 1:
            return True
        else:
            print('"--title" should have only one character to run Feature 3')
    

def is_feature_4(request={}):
    # List all release_dates of a movie.
    expected_keys = ['title', 'release_date']
    key_arguments = get_keys_not_none_arguments(request)
    if expected_keys == key_arguments:
        return True


def is_feature_5(request={}):
    # List All tags for a movie.
    expected_keys = ['title', 'tag']
    key_arguments = get_keys_not_none_arguments(request)
    if expected_keys == key_arguments:
        return True


def is_feature_6(request={}):
    # List all movies with rating n.
    expected_keys = ['rating']
    key_arguments = get_keys_not_none_arguments(request)
    if expected_keys == key_arguments:
        return True


def is_feature_7(request={}):
    # Show all available genres.
    expected_keys = ['genre']
    key_arguments = get_keys_not_none_arguments(request)
    if expected_keys == key_arguments:
        return True


def is_feature_8(request={}):
    # Movies rated by user.
    expected_keys = ['rating', 'user']
    key_arguments = get_keys_not_none_arguments(request)
    if expected_keys == key_arguments:
        return True


if __name__ == '__main__':
    
    print(is_feature_2({
        'title' : 'm1' ,
        'order' : 'sdf',
        'order_by' : 3,
        'genre' : None,
        'release_date' : None,
        'tag' : None,
        'rating' : None,
        'user' : None,
    }))
    print(is_feature_3({
        'title' : 'm' ,
        'order' : None,
        'order_by' : None,
        'genre' : 's',
        'release_date' : None,
        'tag' : None,
        'rating' : None,
        'user' : None,
    }))
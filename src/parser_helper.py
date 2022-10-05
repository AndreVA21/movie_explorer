import argparse


def create_new_parser():
    parser = argparse.ArgumentParser(description='Movies Explorer App,'
                                     'explore the Movies, Raitings y tags.')
    parser.add_argument('-t', '--title', type=str, help='Title of a movie. (a, avengers)',
                        default=None, required=False)
    parser.add_argument('-o', '--order', type=str, help='Order to show the results, (asc | desc).',
                        default=None, required=False,
                        choices=['asc', 'desc', 'ascendent', 'descendent'])
    parser.add_argument('-b', '--by', type=str, help='property on which it is sorted.',
                        choices=['title', 'release date', 'count'],
                        default=None, required=False)
    parser.add_argument('-g', '--genre', type=str, help='Genre of the movies. (Animation)',
                        default=None, required=False)
    parser.add_argument('-rd', '--release_date', type=int,
                        help='Release date of the movies. (1954)',
                        default=None, required=False)
    parser.add_argument('-tg', '--tag', type=str, help='Tags  of the movies. (Tom Cruise)',
                        default=None, required=False)
    parser.add_argument('-r', '--rating', type=float, help='Rating of the movies. (3.0)',
                        default=None, required=False)
    parser.add_argument('-u', '--user', type=int, help="User's id. (1234)",
                        default=None, required=False)

    args = parser.parse_args()

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
    return request

from src.parser_helper import create_new_parser

# Read the Argument Since the console
req = create_new_parser()    # We get the arguments.
# It returns a Dictionary with the formar:
# {
#     'title' : args.title ,
#     'order' : args.order,
#     'order_by' : args.by,
#     'genre' : args.genre,
#     'release_date' : args.release_date,
#     'tag' : args.tag,
#     'rating' : args.rating,
#     'user' : args.user,
# }
if req:
    if req.get('title') and len(req.get('title')) > 1 and \
        req.get('order') and req.get('order_by'):
        # For feature 2 do here
        print('feature 2')
        pass
    elif req.get('title') and len(req.get('title')) == 1 and \
        req.get('order') and req.get('order_by'):
        # For feature 3 do here
        print('feature 3')
    else:
        print('Te arguments are not te corrects',
              'to more information type "movies_explorer.py --help"')
else:
    print('Yo did not type any value for the arguments',
          'to more information type "movies_explorer.py --help"')

import uuid
import json
from src.parser_helper import *
from src.output_helper import save_output_in_json_csv_file
from src.feature_2 import feature_2
from src.feature_3 import feature_3
from src.feature_4 import feature_4
from src.feature_5 import feature_5
from src.feature_7 import feature_7
from src.feature_8 import feature_8
from src.feature_6 import feature_6

# Read the Argument Since the console
req, str_args = create_new_parser()    # We get the arguments in a dict and str.
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
# And str_args the arguments in the following format:
#   "movies_explorer.py --title Step Brothers --tag all"
if req:
    output = []
    if is_feature_2(req):
        output = feature_2(req.get('order'),req.get('order_by'))
        
    elif is_feature_3(req):
        output = feature_3(req.get('title'), req.get('genre'))
        
    elif is_feature_4(req):
        output = feature_4(req.get('title'))

    elif is_feature_5(req):
        output = feature_5(req.get('title'),req.get('tag'))

    elif is_feature_6(req):
        output = feature_6(req.get('rating'))

    elif is_feature_7(req):
        output = feature_7(req)

    elif is_feature_8(req):
        output = feature_8(req)

    else:
        print('The arguments are not te corrects',
              'to more information type "movies_explorer.py --help"')
    
    # Create a unique id.
    unique_id = uuid.uuid4().hex
    # Give the format of the output required.
    dict_output = {
        'request_id': unique_id,
        'data': output,
        'size': len(output)
    }
    # Print with json format
    json_output = json.dumps(dict_output, indent=4)
    print(json_output)
    # Save the result in request.csv and as a json file
    save_output_in_json_csv_file(str_args, dict_output, unique_id)
    
else:
    print('Yo did not type any value for the arguments',
          'to more information type "movies_explorer.py --help"')

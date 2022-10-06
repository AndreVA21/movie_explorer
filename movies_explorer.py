from textwrap import indent
import uuid
import json
from src.parser_helper import create_new_parser, is_feature_2, is_feature_3, is_feature_4, \
    is_feature_5, is_feature_6, is_feature_7, is_feature_8
from src.output_helper import save_output_in_json_csv_file
from components.dict_handler import filter_by_all_title_decen_acend

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
if req:
    output = []
    if is_feature_2(req):
        output = filter_by_all_title_decen_acend(req.get('order'),req.get('order_by'))
        # For feature 2 do here[{sa},{wqer}].
        print('feature 2')
        # output = feature2(req) 
        
    elif is_feature_3(req):
        # For feature 3 do here.
        print('feature 3')
        # output = feature2(req) output wait for a list of dicts [{..},{..}].
        
    elif is_feature_4(req):
        # For feature 3 do here.
        print('feature 4')
        # output = feature2(req) output wait for a list of dicts [{..},{..}].

    elif is_feature_5(req):
        # For feature 3 do here.
        print('feature 5')
        # output = feature5(req) output wait for a list of dicts [{..},{..}].

    elif is_feature_6(req):
        # For feature 3 do here.
        print('feature 6')
        # output = feature6(req) output wait for a list of dicts [{..},{..}].

    elif is_feature_7(req):
        # For feature 3 do here.
        print('feature 7')
        # output = feature7(req) output wait for a list of dicts [{..},{..}].

    elif is_feature_8(req):
        # For feature 3 do here.
        print('feature 8')
        # output = feature8(req) output wait for a list of dicts [{..},{..}].

    else:
        print('The arguments are not te corrects',
              'to more information type "movies_explorer.py --help"')
    
    # example of output
    # output = [
	# 	{
	# 		"title": "ABCDEFG",
	# 		"release_date": 1934,
	# 		"genres": ["acd", "xyz", "fgh"]
	# 	},
	# 	{
	# 		"title": "OPQRST",
	# 		"release_date": 1950,
	# 		"genres": ["acd"]
	# 	}
    # ]
    # Here we are gonna print te ourput as a json and we will add the request to csv
    # and create a new json object with the output content and assigning a uuid.
    unique_id = uuid.uuid4().hex
    dict_output = {
        'request_id': unique_id,
        'data': output,
        'size': len(output)
    }
    json_output = json.dumps(dict_output, indent=4)
    save_output_in_json_csv_file(str_args, dict_output, unique_id)
    print(json_output)
    
else:
    print('Yo did not type any value for the arguments',
          'to more information type "movies_explorer.py --help"')

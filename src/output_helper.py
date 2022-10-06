import csv
import uuid
import json
from datetime import datetime

OUTPUT_PATH = './output/'
REQUEST_FILENAME = 'request.csv'


def write_on_csv_request(request_data):
    answer = {'statusCode': 'error', 'body': None}
    if request_data:
        path = OUTPUT_PATH + REQUEST_FILENAME
        unique_id, date = uuid.uuid4().hex, datetime.now().replace(microsecond=0)
        new_row_data = [unique_id, request_data, date]
        try:
            with open(path, 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(new_row_data)
            answer = {'statusCode': 'ok', 'body': None}
        except Exception as e:
            print('Something bad happened', e)
    return answer


def save_output_in_json_csv_file(str_request, output_data, unique_id):
    answer = {'statusCode': 'error', 'body': None}
    path_csv = OUTPUT_PATH + REQUEST_FILENAME
    path_json = OUTPUT_PATH + unique_id + '.json'
    try:
        current_date = datetime.now().replace(microsecond=0)
        new_row_data = [unique_id, str_request, current_date]
        
        json_data = json.dumps(output_data, indent=4)
        with open(path_csv, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_row_data)
        
        with open(path_json, 'w+') as json_file:
            json_file.write(json_data)
            
        answer = {'statusCode': 'ok', 'body': None}
    except Exception as e:
        print('Something bad happened', e)
    
    return answer

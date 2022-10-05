import csv
import uuid
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

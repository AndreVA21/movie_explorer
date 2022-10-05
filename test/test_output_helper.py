from src.output_helper import write_on_csv_request

OUTPUT_PATH = './output/'
REQUEST_FILENAME = 'request.csv'


def test_write_csv_request_output_returns_ok():
    # Arrange
    filename = REQUEST_FILENAME
    data = f'Test {filename} - ok'
    expected_output = {'statusCode': 'ok', 'body': None}

    # Act
    output = write_on_csv_request(data)

    # Assert
    assert output is not None, 'expected non null response'
    assert type(output) is dict, 'expected response as `dict`'
    assert output == expected_output, 'output did not match expected output'
    assert output.get('statusCode') == 'ok', 'expected `ok` statusCode'
    assert output.get('body') is None, 'expected `None` body'


def test_write_csv_request_not_write_empty_data_returns_error():
    # Arrange
    data = ''
    expected_output = {'statusCode': 'error', 'body': None}

    # Act
    output = write_on_csv_request(data)

    # Assert
    assert output is not None, 'expected non null response'
    assert type(output) is dict, 'expected response as `dict`'
    assert output == expected_output, 'output did not match expected output'
    assert output.get('statusCode') == 'error', 'expected `error` statusCode'
    assert output.get('body') is None, 'expected `None` body'

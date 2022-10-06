from src.file_helper import read_data


def test_read_data_known_filename_returns_non_empty_list():
    file = 'movies'
    extension = 'csv'
    data = read_data(file, extension)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) > 0, 'expected non empty list'


def test_read_data_not_exist_filename_returns_empty_list():
    file = 'not_exist'
    extension = 'csv'
    data = read_data(file, extension)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) == 0, 'expected empty list'

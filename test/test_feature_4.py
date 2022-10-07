from src.feature_4 import feature_4


def test_feature_4_example():
    title = 'Sabrina'
    movie = {
            "title": "Sabrina",
            "release_date": 1995,
            "genres": ["Comedy", "Romance"]
        }
    data = feature_4(title)

    assert type(data) is list, 'expected a list'
    assert movie in data, 'expexted movie Sabrina in data'
    assert len(data) == 2, 'expexted movie Number 2'


def test_feature_4_empty_list():
    title = 'Sabrina example'
    data = feature_4(title)
    assert len(data) == 0, 'expected empty list'

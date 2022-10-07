from src.feature_3 import feature_3


def test_feature_3_empty_list():
    title = 'T'
    genre = 'Animacion'
    data = feature_3(title, genre)
    assert len(data) == 0, 'expexted empty list'
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'

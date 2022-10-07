from src.feature_6 import feature_6


def test_release_date_feature_2():
    rating = '1.0'
    data = feature_6(rating)
    assert len(data) == 2811


def test_release_date_feature_2():
    rating = '0.5'
    data = feature_6(rating)
    assert len(data) == 1370

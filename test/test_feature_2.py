from src.feature_2 import feature_2


def test_release_date_feacture_2():
    order = 'asc'
    order_by = 'release_date'
    data = feature_2(order, order_by)

    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'


def test_release_title_feacture_2():
    order = 'asc'
    order_by = 'title'
    data = feature_2(order, order_by)

    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'

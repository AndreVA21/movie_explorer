from src.feature07 import feature7

def test_feature7_test1():
    genre = "Animation"
    res = {"genre": "all"}
    data = feature7(res)

    assert genre in data, 'expected Animation in list'
    assert type(data) is list, 'expected a list'


def test_feature7_test2():
    res = {"genre": "all"}
    data = feature7(res)

    assert len(data) >= 20, 'expexted list'

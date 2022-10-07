from src.feature05 import feature5

def test_feature5_test1():
    title = "Step Brothers"
    res = "all"
    data = feature5(title,res)

    assert type(data) is list, 'expected a list'
    assert len(data[0]['tags']) == 8, 'expecter len 8'

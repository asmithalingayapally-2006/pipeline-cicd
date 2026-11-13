from app import add

def test_add():
    assert add(10, 20) == 30

def test_add2():
    assert add(5, 5) == 10
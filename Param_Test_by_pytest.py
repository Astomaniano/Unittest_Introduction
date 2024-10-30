import pytest

def check(number):
    return number % 2 == 0

def test_check():
    assert check(2) == True
    assert check(6) == True
    assert check(220)  == True

def test_check_fail():
    assert check(3) == False
    assert check(57) == False

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (6, True),
    (220, True),
    (3, False),
    (57, False)
])

def test_check_param(number, expected):
    assert check(number) == expected

from src.FindSecondMax.util import sec_largest

def test_1():
    assert sec_largest([2, 3, 6, 6, 5]) == 5

def test_2():
    assert sec_largest([91, 81, 71]) == 81

def test_3():
    assert sec_largest([10, 20, 30, 40]) == 30

def test_4():
    assert sec_largest([5, 5, 4, 4, 3]) == 4

def test_5():
    assert sec_largest([-1, -2, -3]) == -2
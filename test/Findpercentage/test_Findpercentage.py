from src.Findpercentage.util import calculate_avg
 
def test_1():
    assert calculate_avg([100,100,100])==100
 
def test_2():
    assert calculate_avg([0,0,0])==0
 
def test_3():
    assert calculate_avg([2,3,4])==3
 
def test_4():
    assert calculate_avg([91,81,71])==81
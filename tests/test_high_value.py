from lib.high_value import *

def test_checks_first_value_high_than_second():
    higher = HighValue(10,5)
    result = higher.get_highest()
    assert result == "First value is higher"

    

def test_increase_first_value():
    increased = HighValue(0,0)
    increased.add(10, "first")
    result = increased.value_first
    assert result == 10 




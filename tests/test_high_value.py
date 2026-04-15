from lib.high_value import *

def test_checks_first_value_high_than_second():
    higher = HighValue(10,5)
    result = higher.get_highest()
    assert result == "First value is higher"

def test_checks_for_lower_value_than_seccond():
    lower = HighValue(5, 10)
    result = lower.get_highest()
    assert result == "Second value is higher"

def test_checks_values_are_equal():
    equal = HighValue(5, 5)
    result = equal.get_highest()
    assert result == "Values are equal"

def test_increase_first_value():
    increased = HighValue(0,0)
    increased.add(10, "first")
    result = increased.value_first
    assert result == 10 

def test_increased_seccond_value():
    increased_seccond = HighValue(5, 0)
    increased_seccond.add(15, "second")
    result = increased_seccond.value_second
    assert result == 15




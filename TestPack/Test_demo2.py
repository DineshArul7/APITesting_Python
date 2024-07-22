# class and method name should always start with test keyword
import pytest

@pytest.mark.skip
def test_firstprogram5():
    print("Deekay")

@pytest.mark.assertion
def test_assertNum2():
    actual = 23
    expected = 12
    assert actual != expected, "Did not match"

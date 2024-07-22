# class and method name should always start with test keyword
import logging

import pytest


@pytest.mark.usefixtures("setup", "beforeClass")
class Test_demo:

    @pytest.mark.xfail
    def test_firstProgram3(self):
        print("Deekay")

    @pytest.mark.xfail
    def test_assertString2(self):
        actual = "Deekay"
        expected = "Devil"
        assert actual == expected, "Did not match"

    @pytest.mark.paramtest
    def test_parameterize(self, get_data):
        print(get_data)



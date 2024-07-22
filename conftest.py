import logging

import pytest


@pytest.fixture
def setup():
    print("I am the setup script")
    yield
    print(("I am the teardown script"))


@pytest.fixture(scope="class")
def beforeClass():
    print("i will execute before class")
    yield
    print("I will run after the class")


@pytest.fixture(params=[1, 2, 3, 4])
def get_data(request):
    return request.param

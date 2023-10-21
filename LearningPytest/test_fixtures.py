import pytest


@pytest.fixture()
def setup():
    print("Open browser")
    print("Login")
    print("find product")

    yield

    print("logoff")
    print("Close browser")

def test_additem(setup):

    print("item added Successful")

def test_removeitem(setup):
    print("item removed Successful")



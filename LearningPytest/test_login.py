import pytest


def testLogin():
    print("Login Successful")

@pytest.mark.sanity
def testLogoff():
    print("Logoff Successful")

@pytest.mark.skip
def testCalculation():
    assert 2+2 == 4


import pytest


def testLogin():
    print("Login Successful")

@pytest.mark.xfail
def testLogoff():
    print("Logoff Successful")
@pytest.mark.xfail
def testCalculation():
    assert 2+2 == 5


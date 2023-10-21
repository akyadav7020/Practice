import pytest

@pytest.mark.regression
def testLogin():
    print("Login Successful")


@pytest.mark.sanity
def testCalculation():
    assert 2+2 == 4


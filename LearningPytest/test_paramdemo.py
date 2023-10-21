import pytest


@pytest.fixture(params=["a","b","c"])
def paramdemo(request):
    print(request.param)


@pytest.mark.parametrize("a,b, sum",[(5,2,7),(2,3,6),(4,9,13)])
def testadddemo(a,b,sum):
    assert a+b == sum


'''def testparam(paramdemo):
    print("success")'''


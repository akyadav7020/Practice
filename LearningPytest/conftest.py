import pytest


#@pytest.fixture()
@pytest.fixture(autouse=True,scope="session")
def tc_setup(browser):
    if browser == "chrome":
        print("open Browser")
    else:
        print("Enter valid browser")
    print("login")
    yield
    print("logOff")
    print("close browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(autouse=True,scope="session")
def browser(request):
    return request.config.getoption("--browser")
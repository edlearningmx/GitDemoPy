import pytest

@pytest.fixture(scope="class")


def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataload():
    print("user profile data is created")
    return("rahul","shetty","rahulshettyacademy.com")

#@pytest.fixture(params=["chrome","firefox","IE"])
#@pytest.fixture(params=[("chrome","Shetty"),"firefox","IE"])
@pytest.fixture(params=[("chrome","Shetty"),("firefox","Rahul"),("IE","Academy")])
def crossBrowser(request):
    return request.param

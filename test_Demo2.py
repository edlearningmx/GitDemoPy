#any pytest file should start with test_ or end with _test
#pytest method should start with test
import pytest


def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "tet failed because strings do not match"
@pytest.mark.smoketest
def test_secondcreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "addition does not match"


@pytest.fixture()
def setup():
    print("i will be executed first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
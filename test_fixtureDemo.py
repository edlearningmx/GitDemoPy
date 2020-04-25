import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute test in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute test in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute test in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute test in fixtureDemo3 method")

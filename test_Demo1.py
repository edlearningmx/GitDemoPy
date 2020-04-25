#any pytest file should start with test_ or end with _test
#pytest method should start with test
#Any code should be wrapped in method only
#method name should be meaningfull
# -k stands for method name execution, -s logs in out put -v for more info metadata
# can run speciic file based on file name
#you can mark (tag) tests @pytest.mark.smoketest and then run with -m
#you can skip with @pytest.mark.skip
#you can not report a TC with @pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases  - conftest file
#to generalize fixture and make it available to all TC's (fixture name into parameters of method)
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoketest
@pytest.mark.skip
def test_firstprogram():
    print("hello")
@pytest.mark.xfail
def test_secondgreetcreditcard():
    print("good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

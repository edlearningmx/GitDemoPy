import pytest

from pyTestDemo.baseClass import baseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(baseClass):

    def test_editProfile(self,dataload):
        log = self.getlogger()
        # print(dataload[0])
        log.info(dataload[0])
        log.info(dataload[2])
        print(dataload[2])

import inspect
import logging

class baseClass:
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logfile.log")
        formater = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formater)
        logger.addHandler(filehandler) #filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
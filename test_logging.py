import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)



    filehandler = logging.FileHandler("logfile.log")
    formater = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formater)
    logger.addHandler(filehandler) #filehandler object
    logger.setLevel(logging.DEBUG)
    logger.debug("a debug statement is executed")
    logger.info("information statement")
    logger.warning("something is in warning mode")
    logger.error("a mayor error has happened")
    logger.critical("critical issue")
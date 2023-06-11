# Writing unit tests for development

import unittest
from db import MongoConnect
import os
from logger import logging

CONF = "testConf."


class DbTest(unittest.TestCase):
    def test_connection(self):
        db:MongoConnect = MongoConnect("testDb", "testCollection")
        print("type of the connection :", type(type(db)))



def checkRequirements():
    """
        Perform the requirement validation
    """
    confFilePath = "./config.ini"
    if not os.path.isfile(confFilePath):
        logging.warning("test")





if __name__ == "__main__":
    # initializing the configuration files for testing if not exist
    checkRequirements()
    # unittest.main()
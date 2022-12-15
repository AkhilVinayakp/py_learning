
'''
Creates a Sample file for interacting with the SQL database

'''

import os
import sqlite3
from sqlite3 import Error
import logging as logger

logger.basicConfig(level=logger.DEBUG, format='%(levelname)s : %(message)s')

class TestData:
    def __init__(self) -> None:
        '''Creates a new database connection
        
        '''
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.Connection("testDB.db")
            self.cursor = self.connection.cursor()
        except Error as e:
            logger.debug("Error in connecting to the database :", e)
        except Exception as e:
            logger.error("Error: ", e)
        finally:
            if self.connection:
                logger.info("Database connection successfull")
            else:
                logger.error("Database connection failed.")

    def creatTable(self, query):
        '''Creates a table 
        :param query: query required to create a table.
        '''
        pass

    def insertData(self, query):
        '''Insert data
        '''
        pass

    






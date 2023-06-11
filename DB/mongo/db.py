
# establishing a mongodb server collection
from pymongo import MongoClient


class MongoConnect:
    '''
    Databse connection establishment
    '''
    def __init__(self, dbname, collection_name) -> None:
        """
        param: dbname : Database name
        collection_name:str 
        """
        try:
            self.__connection: MongoClient = MongoClient("mongodb://localhost:27017")
            avilable_db:list = self.__connection.list_database_names()
            if dbname in avilable_db:
                logging.info(f"using the database..{dbname}")
            else:
                logging.info(f"Creating new database {dbname}")
            self.__db = self.__connection[dbname]
            avilable_collections:list = self.__db.list_collection_names()
            if collection_name in avilable_collections:
                logging.info(f"Using the collection {collection_name}")
            else:
                logging.warning(f"Creating new collection : {collection_name}")
            
        except Exception as e:
            logging.error(f"Can not establish connection")


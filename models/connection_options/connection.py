from pymongo import MongoClient
from .mongo_db_config import mongo_db_infos

class DBConnectionHandler: 
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://mayaragcabral:12345@ac-uviifkt-shard-00-01.qpwswdk.mongodb.net:27017,ac-uviifkt-shard-00-02.qpwswdk.mongodb.net:27017,ac-uviifkt-shard-00-00.qpwswdk.mongodb.net:27017/admin?ssl=true&retryWrites=true&loadBalanced=false&replicaSet=atlas-5o4v36-shard-0&readPreference=primary&connectTimeoutMS=10000&w=majority&authSource=admin&authMechanism=SCRAM-SHA-1'
        self.__database_name = mongo_db_infos["DB_NAME"]
        self.__client = None
        self.__db_connection = None
    
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__client
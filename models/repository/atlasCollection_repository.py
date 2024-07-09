from bson.objectid import ObjectId
from typing import Dict, List


class AtlasCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "admin"
        self.__db_connection = db_connection

    def insert_document(self,document:Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        print(f'EU CONSEGUI INSERIR')
        return document
        
    def salect_many(self) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({})

        for x in data:
            print(x)

    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({
            "cpf": {"$exists": True}
            })

        for x in data: 
            print(x)

    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({
            "$or":[
                {"name":"Lhama"},
                {"nome":{"$exists" : True}}
                ]
            })

        for x in data: 
            print(x)

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({
            '_id': ObjectId('668bd6db98d13f6e9e1af549')
            })

        for x in data:
            print(x)

    def edit_registry(self,name) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one(
            {'_id': ObjectId('668bd6db98d13f6e9e1af549')},
            { "$set" : {"name": name}}
            )
        
        print(data.modified_count)

    def edit_many_registries(self,filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            filtro,
            { "$set" : 
               propriedades
            }
            )
        
        print(data.modified_count)

    def edit_many_increment(self,num) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            {'_id': ObjectId('668bd6db98d13f6e9e1af549')},
            { "$inc" : {"numero": num}}
            )
        
        print(data.modified_count)

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(
            {"Estou" : "inserindo"})
        
        print(data.deleted_count)

    def delete_one_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({
            '_id': ObjectId('668bd6db98d13f6e9e1af549')
            })
        
        print(data.deleted_count)

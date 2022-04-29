from unittest import result
from pymongo import MongoClient
from pprint import pprint

class DataAccess: 
    #Variable de classe
    __username = "root"
    __password = "pass12345"
    __host = "localhost",
    __port = 27017
    __db_name = "DBLP"
    __collection = "publis"

    @classmethod
    def open_connexion(cls):
        #Connexion to DB
        cls.client = MongoClient(username=cls.__username, password=cls.__password, host = cls.__host, port = cls.__port)

        #Select DB
        cls.db_dblp = cls.client[cls.__db_name]

        #Select collection
        cls.publis = cls.db_dblp[cls.__collection]

    @classmethod
    def close_connexion(cls):
        cls.client.close()
    
    @classmethod
    def count_publis(cls):
        cls.open_connexion()
        result = cls.publis.count_documents({})
        cls.close_connexion()
        return result

    
    @classmethod
    def list_books(cls):
        cls.open_connexion()
        books = cls.publis.find({"type":"Book"})
        for b in books:
            print(b)
        cls.close_connexion()

    @classmethod
    def books_2014(cls):
        cls.open_connexion()
        books_2014 = cls.publis.find({"type":"Book", "year":{"$gte":2014}})
        for b in books_2014:
            print(b)
        cls.close_connexion()
    
    @classmethod
    def author_TI(cls):
        cls.open_connexion()
        authors_TI = cls.publis.find({"authors":"Toru Ishida"}, {"_id":0, "title":1, "authors":1})
        for a in authors_TI:
            print(a)
        cls.close_connexion()

    @classmethod
    def distinct_authors(cls):
        cls.open_connexion()
        authors_distinct = cls.publis.distinct("authors")
        for a in authors_distinct:
            print(a)
        cls.close_connexion()

    @classmethod
    def sort_title_TI(cls):
        cls.open_connexion()
        sort_title = cls.publis.find({"authors":"Toru Ishida"}, {"_id":0, "title":1}, sort = [("title", 1)])
        for a in sort_title:
            print(a)
        cls.close_connexion()

    @classmethod
    def count_pub_TI(cls):
        cls.open_connexion()
        count_pub = cls.publis.count_documents({"authors":"Toru Ishida"})
        cls.close_connexion()
        return count_pub

    @classmethod
    def count_pub(cls):
        cls.open_connexion()
        pipeline = [{"$match":{"year":{"$gte":2011}}}, {"$group":{"_id": "$type", "count": {"$sum":1}}}]
        count_pub_2011 = cls.publis.aggregate(pipeline)
        cls.close_connexion()
        return list(count_pub_2011)
    
    @classmethod
    def count_pub_authors(cls):
        cls.open_connexion()
        pipeline = [{"$unwind": "$authors"}, {"$group":{"_id": "$authors", "count": {"$sum":1}}}, {"$sort": {"count": 1}}]
        count_pub_2011 = cls.publis.aggregate(pipeline)
        #cls.close_connexion()
        return list(count_pub_2011)
    




from pymongo import MongoClient
from redis import Redis
import json


redis = Redis(host='redis', port=6379)


class UserDatabase:
    
    def __init__(self):
        # initialize database
        self.client = MongoClient('mongodb://db:27017/')
        self.mydb = self.client["hackit"]
        self.mycol = self.mydb["user_data"]
    
    def get_all_users(self):
        response = self.mycol.find({})
        return response
    
    def write_users(self, issue_data):
        reponse = self.mycol.insert_many(issue_data)
        return reponse
    
    def delete_all_users(self):
        response = self.mycol.delete_many({})
        redis.set('user_id', json.dumps(['ID']))
        return response

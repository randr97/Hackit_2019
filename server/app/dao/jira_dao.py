from pymongo import MongoClient
from redis import Redis
import json


redis = Redis(host='redis', port=6379)


class JiraDatabase:
    
    def __init__(self):
        # initialize database
        self.client = MongoClient('mongodb://db:27017/')
        self.mydb = self.client["hackit"]
        self.mycol = self.mydb["jira_issue_data"]
    
    def write_all_tickets(self, issue_data):
        reponse = self.mycol.insert_many(issue_data)
        return reponse
    
    def delete_all_tickets(self):
        response = self.mycol.delete_many({})
        redis.set('ticket_id', json.dumps(['ID']))
        return response

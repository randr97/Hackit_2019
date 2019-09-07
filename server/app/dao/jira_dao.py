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
    
    def update_status(self, ticket_name, status):
        newvalues = {"$set": {"status.name": status}}
        myquery = {"ticket_name": ticket_name}
        response = self.mycol.update_one(myquery, newvalues)
        return response

    def get_all_tickets(self):
        response = self.mycol.find({})
        return response
    
    def get_ticket_by_name(self,name):
        response = list(self.mycol.find({'ticket_name':name}))
        for i in response:
            del i['_id']
        return response
    
    def get_tickets_id(self,acc_id):
        response = list(self.mycol.find({'assignee.accountId':acc_id}))
        for i in response:
            del i['_id']
        return response
    
    def write_all_tickets(self, issue_data):
        reponse = self.mycol.insert_many(issue_data)
        return reponse
    
    def delete_all_tickets(self):
        response = self.mycol.delete_many({})
        redis.set('ticket_id', json.dumps(['ID']))
        return response

from pymongo import MongoClient


class GitDatabase:
    
    def __init__(self):
        # initialize database
        self.client = MongoClient('mongodb://db:27017/')
        self.mydb = self.client["hackit"]
        self.mycol = self.mydb["git_commit_data"]
    
    def get_all_commits(self):
        data = self.mycol.find()
        return list(data)
    
    def write_all_commits(self, all_commits_status):
        response = self.mycol.insert_many(all_commits_status)
        return response
    
    def delete_all_commits(self):
        response = self.mycol.delete_many({})
        return response
    


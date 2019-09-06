from pymongo import MongoClient


class GitDatabase:
    
    def __init__(self):
        # initialize database
        self.client = MongoClient('mongodb://localhost:27017/')
        self.mydb = self.client["hackit"]
        self.mycol = self.mydb["git_commit_data"]
    
    def write_all_commits(self, all_commits_status):
        try:    
            self.mycol.insert_many(all_commits_status)
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete_all_commits(self):
        try:
            self.mycol.delete_many({})
        except Exception as e:
            print(e)
            return False

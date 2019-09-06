import datetime
import time

from github import Github

from dao.git_dao import GitDatabase

TOKEN = '6d75e9cccad717b4a453b5bf4e945386ef1a7b6d'
REPO_NAME = 'Hackit_2019'

class GitHubJob:
    def __init__(self, user_name='DhruvaPatil98', token=TOKEN, repo_name=REPO_NAME):
        self.user_name = user_name
        self.admin = self.get_admin(token)
        self.repo = self.get_repo(user_name+'/'+repo_name)


    def get_admin(self, token): # Ex: dhruva - 6d75e9cccad717b4a453b5bf4e945386ef1a7b6d, rohit - 80b7b2fbc18b0d6192b19aaffae39aa2058cfc76
        return Github(token)

    def get_repo(self, repo_id_or_name): # Ex: "194830160" or "DhruvaPatil98/alchemy-marketing-ui"
        return self.admin.get_repo(repo_id_or_name)

    def get_commits_in_range(self, **kwargs):
        return self.repo.get_commits(**kwargs)

    def get_commit_stats(self, newcommit, jira_ticket="H2-1"):
        if jira_ticket in newcommit.commit.message:    
            files = newcommit.files
            dict_lang = {
                "additions_python": sum([i.additions for i in files if 'py' in i.filename.split('.')[-1]]),
                "deletions_python": sum([i.deletions for i in files if 'py' in i.filename.split('.')[-1]]),
                "additions_java": sum([i.additions for i in files if 'js' in i.filename.split('.')[-1]]),
                "deletions_java": sum([i.deletions for i in files if 'js' in i.filename.split('.')[-1]]),
                "additions_html": sum([i.additions for i in files if 'html' in i.filename.split('.')[-1]]),
                "deletions_html": sum([i.deletions for i in files if 'html' in i.filename.split('.')[-1]]),
                "additions_css": sum([i.additions for i in files if 'less' in i.filename.split('.')[-1]]),
                "deletions_css": sum([i.deletions for i in files if 'less' in i.filename.split('.')[-1]]),
            }
            stats = {
                "commit_id": newcommit.sha,
                "repo_id": self.repo.id,
                "author_name": newcommit.commit.author.name,
                "author_id": newcommit.author.id,
                "commit_message": newcommit.commit.message,
                "additions": newcommit.stats.additions,
                "deletetions": newcommit.stats.deletions,
                "total": newcommit.stats.total,
                "time": newcommit.commit.author.date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None),
            }
            stats.update(dict_lang)
            return stats
        else:
            return None

    def git_job(self):
        try:
            database_object = GitDatabase()
            all_commits = self.get_commits_in_range(author=self.user_name)
            all_commits_status = []
            for c in all_commits:
                newcommit = self.get_commit_stats(c)
                if newcommit:
                    all_commits_status.append(newcommit)
            print("*********************")
            print(all_commits_status[-1])
            print("*********************")
            database_object.delete_all_commits()
            database_object.write_all_commits(all_commits_status)
            return True
        except Exception as e:
            print(e)
            return False

job_object = GitHubJob()
while 1:
    job_object.git_job()
    time.sleep(1)
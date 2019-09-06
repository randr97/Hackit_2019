import datetime
import time

from github import Github

from dao.git_dao import GitDatabase

TOKEN = '80b7b2fbc18b0d6192b19aaffae39aa2058cfc76'
REPO_NAME = 'Hackit_2019'

class GitHubJob:
    def __init__(self, user_name='DhruvaPatil98', token=TOKEN, repo_name=REPO_NAME):
        self.user_name = user_name
        self.admin = self.get_admin(token)
        self.repo = self.get_repo(user_name+'/'+repo_name)


    def get_admin(self, token): # Ex: dhruva - 1b5dc1829a80dbf083bf38275499808f36a79d7a, rohit - 80b7b2fbc18b0d6192b19aaffae39aa2058cfc76
        return Github(token)

    def get_repo(self, repo_id_or_name): # Ex: "194830160" or "DhruvaPatil98/alchemy-marketing-ui"
        return self.admin.get_repo(repo_id_or_name)

    def get_commits_in_range(self, **kwargs):
        return self.repo.get_commits(**kwargs)

    def get_commit_stats(self, newcommit):
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
        return stats

    def git_job(self):
        try:
            database_object = GitDatabase()
            all_commits = self.get_commits_in_range(author=self.user_name)
            all_commits_status = [self.get_commit_stats(c) for c in all_commits]
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
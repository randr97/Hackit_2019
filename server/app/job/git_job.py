import datetime
import time

from github import Github

from dao.git_dao import GitDatabase

TOKEN = 'f8e47bb8b94f9b27c72931bf9300b31c90137f1d'
REPO_NAME = 'DhruvaPatil98/Hackit_2019'

class GitHubJob:
    def __init__(self, token=TOKEN, repo_name=REPO_NAME):
        self.user = self.get_user(token)
        self.repo = self.get_repo(repo_name)

    def get_user(self, token): # Ex: dhruva - 1b5dc1829a80dbf083bf38275499808f36a79d7a, rohit - f8e47bb8b94f9b27c72931bf9300b31c90137f1d
        return Github(token)

    def get_repo(self, repo_id_or_name): # Ex: "194830160" or "DhruvaPatil98/alchemy-marketing-ui"
        print(self.user.get_repos(), repo_id_or_name)
        return self.user.get_repo(repo_id_or_name)

    def get_commits_in_range(self, **kwargs):
        return self.repo.get_commits(**kwargs)

    def get_commit_stats(self, newcommit):
        stats = {
            "commit_id": newcommit.sha,
            "repo_id": self.repo.id,
            "author_name": newcommit.commit.author.name,
            "commit_message": newcommit.commit.message,
            "additions": newcommit.stats.additions,
            "deletetions": newcommit.stats.deletions,
            "total": newcommit.stats.total,
            "time": newcommit.commit.author.date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None),
        }
        return stats

    def git_job(self):
        try:
            print(1)
            database_object = GitDatabase()
            all_commits = self.get_commits_in_range()
            all_commits_status = [self.get_commit_stats(c) for c in all_commits]
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
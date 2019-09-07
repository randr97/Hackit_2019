from dao.git_dao import GitDatabase

class GitServices:
    def __init__(self, ticket_name, git_id):
        self.git_id = git_id
        self.ticket_name = ticket_name
        self.git_commits = GitDatabase().get_commits_from_user(ticket_name, git_id)

    def get_time_commit(self):
        graph_data = {
            "additions": [],
            "deletions": [],
            "additions_python": [],
            "deletions_python": [],
            "additions_java": [],
            "deletions_java": [],
            "additions_html": [],
            "deletions_html": [],
            "additions_css": [],
            "deletions_css": [],
        }
        for i in self.git_commits:
            graph_data["additions"].append([i["additions"], i["time"]])
            graph_data["deletions"].append([i["deletions"], i["time"]])
            graph_data["additions_python"].append([i["additions_python"], i["time"]])
            graph_data["deletions_python"].append([i["deletions_python"], i["time"]])
            graph_data["additions_java"].append([i["additions_java"], i["time"]])
            graph_data["deletions_java"].append([i["deletions_java"], i["time"]])
            graph_data["additions_html"].append([i["additions_html"], i["time"]])
            graph_data["deletions_html"].append([i["deletions_html"], i["time"]])
            graph_data["additions_css"].append([i["additions_css"], i["time"]])
            graph_data["deletions_css"].append([i["deletions_css"], i["time"]])
        return graph_data
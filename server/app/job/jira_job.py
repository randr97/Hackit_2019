from jira.client import JIRA
from redis import Redis
from dao.jira_dao import JiraDatabase
from dao.user_dao import UserDatabase
import logging
import schedule
import time
import json

redis = Redis(host='redis', port=6379)
redis.set('ticket_id', json.dumps(['ID']))
redis.set('user_id', json.dumps(['ID']))

StatusCodes = {
    'To Do': 11,
    'In Progress': 21,
    'Done': 31,
}

PROJECT_URL="https://bitsandbytes.atlassian.net"
ADMIN_ID="rohitshrothrium.ss1997@gmail.com"
AUTH_TOKEN="3kyiChzvatMWEJ6aGri0EF0F"

log = logging.getLogger(__name__)

class JiraJob:
    def get_issues(self,jc):
        print("Calling job ==========>")  
        projects = jc.projects()
        issues_final = []
        # user_final = []
        for v in projects:
            issues_in_proj = jc.search_issues(f'project={v.key}')
            for issues in issues_in_proj:
                cache_ticket = json.loads(redis.get('ticket_id'))
                if issues.id not in cache_ticket:
                    print("mofo")
                    cache_ticket.append(issues.id)
                    redis.set('ticket_id', json.dumps(cache_ticket))
                    issue_temp = {
                        'issue_id': issues.id,
                        'ticket_name': issues.key,
                        'created_on': issues.fields.created,
                        'status': dict(issues.fields.status.raw),
                        'assignee': dict(issues.fields.assignee.raw),
                        'start_time':'',
                        'end_time':'',
                        'pause_time':'',
                        'total_time_spent':'',
                        'commits':[]
                    }
                    issues_final.append(issue_temp)
                    cache_user = json.loads(redis.get('user_id'))
                    print('=======>', cache_user)
                    if issues.fields.assignee.accountId not in cache_user:
                        print("mofo2")
                        cache_user.append(issues.fields.assignee.accountId)
                        redis.set('user_id', json.dumps(cache_user))
                        # user_final.append(dict(issues.fields.assignee.raw))

        # if(len(user_final) > 0):
        #     to_mongo = UserDatabase()
        #     print('USER To mongo ==========>', user_final)
        #     response = to_mongo.write_users(user_final)
        #     print('USER Mongo Response ==========>', response)
        if(len(issues_final) > 0):
            to_mongo = JiraDatabase()
            print('TICKET To mongo ==========>', issues_final)
            response = to_mongo.write_all_tickets(issues_final)
            print('TICKET Mongo Response ==========>', response)


    # Defines a function for connecting to Jira
    def connect_jira(self,log, jira_server, jira_user, jira_password):
        '''
        Connect to JIRA. Return None on error
        '''
        try:
            log.info("Connecting to JIRA: %s" % jira_server)
            jira_options = {'server': jira_server}
            jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
                                            # ^--- Note the tuple
            return jira
        except e:
            log.error("Failed to connect to JIRA: %s" % e)
            return None

    def update_status(self, ticket_name, status):
        jc = self.connect_jira(log, PROJECT_URL, ADMIN_ID, AUTH_TOKEN)
        issue = jc.issue(ticket_name)
        response = jc.transition_issue(issue, StatusCodes[status])
        return response

    def job(self):
        jc = self.connect_jira(log, PROJECT_URL, ADMIN_ID, AUTH_TOKEN)
        self.get_issues(jc)


jj = JiraJob()
jj.job()

# while 1:
#     jj.job()
#     time.sleep(1)

from jira.client import JIRA
import logging
import schedule
import time
from redis import Redis
import json

redis = Redis(host='redis', port=6379)
redis.set('ticket_id', json.dumps(['ID']))

# get issues
def get_issues(jc):    
    projects = jc.projects()
    issues_final = []
    for v in projects:
        issues_in_proj = jc.search_issues(f'project={v.key}')
        for issues in issues_in_proj:
            cache = json.loads(redis.get('ticket_id'))=
            if issues.id not in cache:
                print("mofo")
                cache.append(issues.id)
                redis.set('ticket_id', json.dumps(cache))
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
    print('To mongo ==========>', issues_final)
    return issues_final


# Defines a function for connecting to Jira
def connect_jira(log, jira_server, jira_user, jira_password):
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

log = logging.getLogger(__name__)

def job():
    jc = connect_jira(log, "https://bitsandbytes.atlassian.net", "rohitshrothrium.ss1997@gmail.com", 
    "3kyiChzvatMWEJ6aGri0EF0F")
    get_issues(jc)

schedule.every(5).minutes.do(job())
# while 1:
#     job()
#     time.sleep(1)
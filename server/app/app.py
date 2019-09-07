# compose_flask/app.py
import os
import flask
from redis import Redis
from dao.git_dao import GitDatabase
from dao.jira_dao import JiraDatabase
from dao.user_dao import UserDatabase
from flask_cors import CORS
from werkzeug import secure_filename
from job.jira_job import JiraJob
from services.git_services import GitServices
from services.enum import StatusEnum

app = flask.Flask(__name__,static_url_path='/code/uploads')
redis = Redis(host='redis', port=6379)
CORS(app)

@app.route('/users', methods=["GET"])
def users():
    user = UserDatabase()
    response = user.get_all_users()
    return flask.jsonify({"result": response})


@app.route('/users/<acc_id>', methods=["GET"])
def jira_tickets(acc_id):
    ticket = JiraDatabase()
    response = ticket.get_tickets_id(acc_id)
    return flask.jsonify({"tickets": response})

@app.route('/users/<acc_id>/<ticket_name>', methods=["GET"])
def git_commits(acc_id, ticket_name):
    ticket = JiraDatabase()
    ticket_info = ticket.get_ticket_by_name(ticket_name)
    github_object = GitDatabase()
    user_object = UserDatabase()
    git_id = user_object.get_user_id(acc_id)[0].get('github_id')
    github_service = GitServices(ticket_name, git_id)
    git_commits = github_object.get_commits_from_user(ticket_name, git_id)
    graph_data = github_service.get_time_commit()
    return flask.jsonify({"ticket_info": ticket_info, "git_commits": git_commits, "graph_data": graph_data})

@app.route('/upload', methods=['POST'])
def upload():
    file = flask.request.files['file']
    file.save(os.path.abspath(f'uploads/{file.filename}'))
    return flask.jsonify({"message": "success"})

@app.route('/get/<path:path>')
def send_png(path):
    return flask.send_from_directory(directory='/code/uploads/', filename=path)

@app.route('/status',methods=["PUT"])
def status_change():
    ticket_name = flask.request.json['ticket_name']
    status = flask.request.json['status']
    jira_object = JiraDatabase()
    jira_job = JiraJob()
    if status in [StatusEnum.DONE, StatusEnum.INPROGRESS]:
        response = jira_object.update_status(ticket_name, status)
        jira_job.update_status(ticket_name, status)
    else:
        response = jira_object.update_status(ticket_name, status)
    return {"result": str(response)}

# @app.route('/gitcommits', methods=["GET"])
# def git_commits():
#     git_dao_object = GitDatabase()
#     return flask.jsonify({"result": git_dao_object.get_all_commits()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
# compose_flask/app.py
import flask
from redis import Redis
from dao.git_dao import GitDatabase
from dao.jira_dao import JiraDatabase


app = flask.Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/users', methods=["GET"])
def users():
    user = UserDatabase()
    response = user.get_all_users()
    return flask.jsonify({"result": response})


@app.route('/users/<acc_id>', methods=["GET"])
def jira_tickets(acc_id):
    ticket = JiraDatabase()
    response = ticket.get_tickets_id(acc_id)
    return flask.jsonify({"user_info": response})

@app.route('/users/<acc_id>/<ticket_name>', methods=["GET"])
def jira_tickets(acc_id, ticket_name):
    ticket = JiraDatabase()
    response = ticket.get_tickets_id(acc_id)
    return flask.jsonify({"user_info": response})
    

@app.route('/gitcommits', methods=["GET"])
def git_commits():
    git_dao_object = GitDatabase()
    return flask.jsonify({"result": git_dao_object.get_all_commits()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
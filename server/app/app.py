# compose_flask/app.py
import flask
from redis import Redis
from dao.git_dao import GitDatabase
from dao.user_dao import UserDatabase


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/users')
def users():
    user = UserDatabase()
    user.get_all_users()
    

@app.route('/gitcommits', methods=["GET"])
def git_commits():
    git_dao_object = GitDatabase()
    return flask.jsonify({"result": git_dao_object.get_all_commits()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
# compose_flask/app.py
from flask import Flask
from redis import Redis
from dao.git_dao import GitDatabase

app = Flask(__name__)

redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/gitcommits/')
def git_commits():
    git_dao_object = GitDatabase()
    return git_dao_object.get_all_commits()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
import json
import os

import flask
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from quiz.models import Quiz
from quiz.QuizController import QuizController
from quiz.CacheStorageRepository import CacheStorageRepository
from quiz.StorageRepository import StorageRepository
from sql.SQLStorageRepository import SQLStorageRepository
from sql.database import db_session

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

config_filename = f"config.{os.environ['MODE']}.json"
app.config.from_file(config_filename, json.load)

repo: StorageRepository = CacheStorageRepository()

if app.config['STORAGE'] == "SQL":
    repo = SQLStorageRepository()


quizController: QuizController = QuizController(repo)

@app.route('/')
def hello_world():
    return 'Hello World!!!!'


@app.route("/api/quiz", methods=['POST'])
def test_quiz_route():
    quiz_name: str = flask.request.json['name']
    quiz: Quiz = quizController.create_quiz(quiz_name)
    app.logger.info(f'"{quiz.name}" successfully created')
    app.logger.info(f'"{quiz.id}" testing uuid generation')
    return {"Status": "Successful", "quiz": quiz.__dict__}, 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host=app.config["LISTEN_TO"], debug=app.config["DEBUG"])





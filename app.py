import json
import os
from typing import List
from uuid import UUID

import flask
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from quiz.models import Quiz, Question, AnswerOption
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

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        if isinstance(obj, Quiz):
            return obj.__dict__
        if isinstance(obj, Question):
            return obj.__dict__
        if isinstance(obj, AnswerOption):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

@app.route('/')
def hello_world():
    return 'Hello World!!!!'


@app.route("/api/quiz", methods=['POST'])
def quiz_create_route():
    quiz_name: str = flask.request.get_json()['name']
    quiz: Quiz = quizController.create_quiz(quiz_name)
    app.logger.info(f'"{quiz.name}" successfully created')
    return {"status": "success", "quiz": quiz.__dict__}, 200


@app.route("/api/quiz/all", methods=['GET'])
def quiz_get_route():
    amount: int = int(flask.request.args.get("amount"))
    offset: int = int(flask.request.args.get("offset"))
    app.logger.info(f'Numbers of quizzes requested - Amount: {amount} & Offset: {offset}')
    quizzes: List[Quiz] = quizController.get_quizzes(offset, amount)
    response = app.response_class(
        response=json.dumps(quizzes, cls=Encoder),
        status=200,
        mimetype='application/json'
    )
    return response


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host=app.config["LISTEN_TO"], debug=app.config["DEBUG"])





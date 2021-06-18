import flask
from flask import Flask
from flask_restful import Api

from quiz.adapters.CacheStorageRepository import CacheStorageRepository
from quiz.models import Quiz
from quiz.use_cases.QuizController import QuizController
from quiz.use_cases.StorageRepository import StorageRepository

app = Flask(__name__)
api = Api(app)

repo: StorageRepository = CacheStorageRepository()
quizController: QuizController = QuizController(repo)


@app.route('/')
def hello_world():
    return 'Hello World!!!!'


@app.route("/api/quiz", methods=['POST'])
def test_quiz_route():
    quiz_name: str = flask.request.json['name']
    quiz: Quiz = quizController.create_quiz(quiz_name)
    app.logger.info(f'"{quiz.name}" successfully created')
    return {"Status": "Successful", "quiz": quiz.__dict__}, 200


if __name__ == '__main__':
    app.run()




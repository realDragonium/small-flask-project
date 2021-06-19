import uuid
from typing import List

from quiz.StorageRepository import StorageRepository
from quiz.models import Quiz, Question, AnswerOption
from sql.database import db_session, init_db
from sql.sql_models import SQLQuiz, SQLQuestion, SQLAnswerOption


class SQLStorageRepository(StorageRepository):

    def __init__(self):
        init_db()

    def save_quiz(self, quiz: Quiz):
        sql_quiz: SQLQuiz = quiz_to_sql_quiz(quiz)
        db_session.add(sql_quiz)
        db_session.commit()

    def get_quiz(self, quiz_id: uuid) -> Quiz:
        sql_quiz: SQLQuiz = SQLQuiz.query.filter(SQLQuiz.id == quiz_id).first()
        return sql_quiz_to_quiz(sql_quiz)

    def get_question(self, question_id: uuid.UUID) -> Question:
        sql_question: SQLQuestion = SQLQuestion.query.filter(SQLQuestion.id == question_id).first()
        return sql_question_to_question(sql_question)

    def update_quiz(self, quiz: Quiz):
        sql_quiz: SQLQuiz = quiz_to_sql_quiz(quiz)

    def get_quizzes(self, offset: int, amount: int) -> List[Quiz]:
        pass

    def get_newest_quiz(self) -> Quiz:
        sql_quiz: SQLQuiz = SQLQuestion.query.all()[0]
        return sql_quiz_to_quiz(sql_quiz)



def quiz_to_sql_quiz(quiz: Quiz) -> SQLQuiz:
    questions: List[SQLQuestion] = [question_to_sql_question(question) for question in quiz.questions]
    return SQLQuiz(quiz.id, quiz.name, questions)


def question_to_sql_question(question: Question) -> SQLQuestion:
    answers: List[SQLAnswerOption] = [answer_option_to_sql_answer_option(option) for option in question.answer_options]
    return SQLQuestion(question.id, question.text, answers)


def answer_option_to_sql_answer_option(answer_option: AnswerOption) -> SQLAnswerOption:
    return SQLAnswerOption(answer_option.id, answer_option.text, answer_option.is_correct)


def sql_quiz_to_quiz(quiz: SQLQuiz) -> Quiz:
    questions: List[Question] = [sql_question_to_question(question) for question in quiz.questions]
    return Quiz(quiz.name, questions, quiz.id)


def sql_question_to_question(question: SQLQuestion) -> Question:
    answers: List[AnswerOption] = [sql_answer_option_to_answer_option(option) for option in question.answer_options]
    return Question(question.text, answers, question.id)


def sql_answer_option_to_answer_option(answer_option: SQLAnswerOption) -> AnswerOption:
    return AnswerOption(answer_option.text, answer_option.is_correct, answer_option.id)


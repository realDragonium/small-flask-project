import uuid
from typing import List

from quiz.StorageRepository import StorageRepository
from quiz.models import Quiz, Question, AnswerOption

default_quiz_amount: int = 25


class QuizController:

    def __init__(self, repo: StorageRepository):
        self.repository = repo

    def create_quiz(self, name: str) -> Quiz:
        new_quiz = Quiz(name)
        self.repository.save_quiz(new_quiz)
        return new_quiz

    def add_question_to_quiz(self, quiz_id: uuid.UUID, question: Question) -> None:
        quiz = self.repository.get_quiz(quiz_id)
        quiz.add_question(question)
        self.repository.update_quiz(quiz)

    def get_correct_answer_for_question(self, question_id: uuid.UUID) -> List[AnswerOption]:
        question = self.repository.get_question(question_id)
        correct_answers: List[AnswerOption] = []
        for answer in question.answer_options:
            if answer.is_correct:
                correct_answers.append(answer)
        return correct_answers

    def get_quizzes(self, offset: int = 0, amount: int = default_quiz_amount):
        if offset is None or offset < 0:
            offset = 0
        if amount is None or amount < 0:
            amount = default_quiz_amount
        quizzes: List[Quiz] = self.repository.get_quizzes(offset, amount)
        return quizzes






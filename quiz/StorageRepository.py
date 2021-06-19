import uuid
from typing import List

from quiz.models import Quiz, Question


class StorageRepository:
    def save_quiz(self, quiz: Quiz):
        pass

    def update_quiz(self, quiz: Quiz):
        pass

    def get_quiz(self, quiz_id: uuid) -> Quiz:
        pass

    def get_question(self, question_id: uuid.UUID) -> Question:
        pass

    def get_quizzes(self, offset: int, amount: int) -> List[Quiz]:
        pass


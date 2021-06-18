import uuid
from typing import Dict, List

from quiz.models import Quiz, Question
from quiz.use_cases.StorageRepository import StorageRepository


class CacheStorageRepository(StorageRepository):
    def __init__(self):
        self.storage: Dict[uuid.UUID, Quiz] = {}
        self.newest_quiz: Quiz = Quiz()

    def save_quiz(self, quiz: Quiz):
        self.storage[quiz.id] = quiz
        self.newest_quiz = quiz

    def get_quiz(self, quiz_id: uuid) -> Quiz:
        return self.storage[quiz_id]

    def get_newest_quiz(self) -> Quiz:
        return self.newest_quiz

    def get_question(self, question_id: uuid.UUID) -> Question:
        for key, quiz in self.storage.items():
            for question in quiz.questions:
                if question.id == question_id:
                    return question

    def get_quizzes(self, offset: int, amount: int) -> List[Quiz]:
        quizzes: List[Quiz] = []
        loop_counter: int = 0
        for key, quiz in self.storage.items():
            if loop_counter >= offset:
                quizzes.append(quiz)
                if len(quizzes) == amount:
                    break
            loop_counter += 1
        return quizzes

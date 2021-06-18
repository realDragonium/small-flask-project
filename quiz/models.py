import uuid
from typing import List


class AnswerOption:
    def __init__(self, text: str = "default initialization value", is_correct: bool = False):
        self.id: uuid.UUID = uuid.uuid4()
        self.text: str = text
        self.is_correct: bool = is_correct


class Question:
    def __init__(self, question: str, answer_options: List[AnswerOption]):
        self.text: str = question
        self.id: uuid.UUID = uuid.uuid4()
        self.answer_options: List[AnswerOption] = answer_options


class Quiz:
    def __init__(self, name: str = 'nameless'):
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.questions: List[Question] = []

    def add_question(self, question: Question) -> None:
        self.questions.append(question)

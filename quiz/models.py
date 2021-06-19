import uuid
from typing import List


class AnswerOption:
    def __init__(self, text: str = "default initialization value", is_correct: bool = False, old_id: uuid.UUID = None):

        if old_id is None:
            self.id = uuid.uuid4()
        else:
            self.id: uuid.UUID = old_id
        self.text: str = text
        self.is_correct: bool = is_correct


class Question:
    def __init__(self, question: str, answer_options: List[AnswerOption], id: uuid.UUID = None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id: uuid.UUID = id
        self.text: str = question
        self.answer_options: List[AnswerOption] = answer_options


class Quiz:
    def __init__(self, name: str = 'nameless', questions: List[Question] = None, id: uuid.UUID = None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id: uuid.UUID = id
        self.name: str = name
        if questions is None:
            self.questions: List[Question] = []
        else:
            self.questions: List[Question] = questions

    def add_question(self, question: Question) -> None:
        self.questions.append(question)


from uuid import UUID,  uuid4
from typing import List


class AnswerOption:
    def __init__(self, text: str = "default initialization value", is_correct: bool = False, its_id: UUID = None):
        if its_id is None:
            self.id = uuid4()
        else:
            self.id: UUID = its_id
        self.text: str = text
        self.is_correct: bool = is_correct


class Question:
    def __init__(self, question: str, answer_options: List[AnswerOption], its_id: UUID = None):
        if its_id is None:
            self.id = uuid4()
        else:
            self.id: UUID = its_id
        self.text: str = question
        if answer_options is None:
            self.answer_options: List[AnswerOption] = []
        else:
            self.answer_options: List[AnswerOption] = answer_options


class Quiz:
    def __init__(self, name: str = 'nameless', questions: List[Question] = None, its_id: UUID = None):
        if its_id is None:
            self.id = uuid4()
        else:
            self.id: UUID = its_id
        self.name: str = name
        if questions is None:
            self.questions: List[Question] = []
        else:
            self.questions: List[Question] = questions

    def add_question(self, question: Question) -> None:
        self.questions.append(question)


import uuid
from typing import List

from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from sql.database import Base


class SQLAnswerOption(Base):
    __tablename__ = 'answer_option'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey('question.id'))
    text = Column(String)
    is_correct = Column(Boolean)

    def __init__(self, id: uuid.UUID, text: str, is_correct: bool, question_id: uuid.UUID):
        self.id: uuid.UUID = id
        self.text: str = text
        self.is_correct: bool = is_correct
        self.question_id: uuid.UUID = question_id


class SQLQuestion(Base):
    __tablename__ = 'question'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey('quiz.id'))
    text = Column(String)
    answer_options = relationship(SQLAnswerOption, backref='question', lazy='joined')

    def __init__(self, id: uuid.UUID, text: str, answer_options: List[SQLAnswerOption], quiz_id: uuid.UUID):
        self.text: str = text
        self.id: uuid.UUID = id
        self.quiz_id: uuid.UUID = quiz_id
        if answer_options is None:
            self.answer_options: List[SQLAnswerOption] = []
        else:
            self.answer_options: List[SQLAnswerOption] = answer_options


class SQLQuiz(Base):
    __tablename__ = 'quiz'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    questions = relationship(SQLQuestion, backref='quiz', lazy='joined')

    def __init__(self, id: uuid.UUID, name: str, questions: List[SQLQuestion]):
        self.id: uuid.UUID = id
        self.name: str = name
        if questions is None:
            self.questions: List[SQLQuestion] = []
        else:
            self.questions: List[SQLQuestion] = questions

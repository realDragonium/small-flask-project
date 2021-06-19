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

    def __init__(self, id: uuid.UUID, text: str, is_correct: bool = False):
        self.id: uuid.UUID = id
        self.text: str = text
        self.is_correct: bool = is_correct


class SQLQuestion(Base):
    __tablename__ = 'question'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey('quiz.id'))
    text = Column(String)
    answer_options = relationship(SQLAnswerOption, backref='question')

    def __init__(self, id: uuid.UUID, text: str, answer_options: List[SQLAnswerOption]):
        self.text: str = text
        self.id: uuid.UUID = id
        self.answer_options: List[SQLAnswerOption] = answer_options


class SQLQuiz(Base):
    __tablename__ = 'quiz'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    questions = relationship(SQLQuestion, backref='quiz')

    def __init__(self, id: uuid.UUID, name: str, questions: List[SQLQuestion]):
        self.id: uuid.UUID = id
        self.name: str = name
        self.questions: List[SQLQuestion] = questions

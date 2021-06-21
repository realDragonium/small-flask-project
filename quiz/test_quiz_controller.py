import unittest
from typing import List

from quiz.QuizController import QuizController, default_quiz_amount
from quiz.StorageRepository import StorageRepository
from quiz.models import Quiz, Question, AnswerOption


class TestQuizController(unittest.TestCase):

    def __init__(self, testName, repo: StorageRepository):
        super(TestQuizController, self).__init__(testName)
        self.repo: StorageRepository = repo

    def setUp(self):
        self.controller: QuizController = QuizController(self.repo)

    def tearDown(self) -> None:
        self.repo.teardown_test_data()

    def create_quiz(self, name: str = "Best quiz") -> Quiz:
        return self.controller.create_quiz(name)

    def test_creation_QuizController(self):
        self.assertIsInstance(self.controller, QuizController, "Test or controller is of type QuizController")

    def test_create_new_Quiz(self):
        name: str = "Best quiz"
        new_quiz: Quiz = self.controller.create_quiz(name)
        self.assertEqual(new_quiz.name, name, "Should have the same name")

    def test_add_question_to_quiz(self):
        new_quiz: Quiz = self.create_quiz()
        question = create_question()
        self.controller.add_question_to_quiz(new_quiz.id, question)
        post_insert_quiz = self.repo.get_quiz(new_quiz.id)
        self.assertEqual(1, len(post_insert_quiz.questions))

    def test_get_correct_answer_for_question(self):
        new_quiz: Quiz = self.create_quiz()
        question: Question = create_question()
        self.controller.add_question_to_quiz(new_quiz.id, question)

        correct_answers = self.controller.get_correct_answer_for_question(question.id)
        self.assertEqual(len(correct_answers), 1)

    def test_get_correct_answers_for_question(self):
        new_quiz: Quiz = self.create_quiz()
        question: Question = create_question()
        for answer_option in question.answer_options:
            answer_option.is_correct = True
        self.controller.add_question_to_quiz(new_quiz.id, question)

        correct_answers = self.controller.get_correct_answer_for_question(question.id)
        self.assertEqual(len(correct_answers), 4)

    def test_get_request_amount_of_quizzes_when_available(self):
        expected_number_of_quizzes: int = 15
        for i in range(20):
            self.create_quiz()

        quizzes: List[Quiz] = self.controller.get_quizzes(offset=0, amount=expected_number_of_quizzes)
        self.assertEqual(expected_number_of_quizzes, len(quizzes))

    def test_get_less_than_request_amount_of_quizzes_when_less_is_available(self):
        request_amount: int = 15
        expected_number_of_quizzes: int = 7
        for i in range(7):
            self.create_quiz()

        quizzes: List[Quiz] = self.controller.get_quizzes(amount=request_amount)
        self.assertEqual(expected_number_of_quizzes, len(quizzes))

    def test_get_less_than_request_amount_of_quizzes_when_less_is_available_with_offset(self):
        request_amount: int = 15
        expected_number_of_quizzes: int = 2
        for i in range(7):
            self.create_quiz()

        quizzes: List[Quiz] = self.controller.get_quizzes(offset=5, amount=request_amount)
        self.assertEqual(expected_number_of_quizzes, len(quizzes))

    def test_negative_offset_will_be_ignored(self):
        request_amount: int = 10
        expected_number_of_quizzes: int = 10
        for i in range(15):
            self.create_quiz()

        quizzes: List[Quiz] = self.controller.get_quizzes(offset=-5, amount=request_amount)
        self.assertEqual(expected_number_of_quizzes, len(quizzes))

    def test_negative_amount_will_result_to_default_amount(self):
        request_amount: int = -10
        expected_number_of_quizzes: int = default_quiz_amount
        for i in range(30):
            self.create_quiz()

        quizzes: List[Quiz] = self.controller.get_quizzes(offset=-5, amount=request_amount)
        self.assertEqual(expected_number_of_quizzes, len(quizzes))

    def test_get_quizzes_with_None(self):
        expected_number_of_quizzes: int = default_quiz_amount
        for i in range(30):
            self.create_quiz()

        quizzes: List[Quiz] = self.controller.get_quizzes(None, None)
        self.assertEqual(expected_number_of_quizzes, len(quizzes))

    def test_add_multiple_questions_to_quiz(self):
        new_quiz: Quiz = self.create_quiz()
        questions: List[Question] = [create_question(), create_question(), create_question()]
        self.controller.add_questions_to_quiz(new_quiz.id, questions)
        post_insert_quiz = self.repo.get_quiz(new_quiz.id)
        self.assertEqual(3, len(post_insert_quiz.questions))


def create_question() -> Question:
    text: str = "Hello new question"
    answer1: AnswerOption = AnswerOption(is_correct=True)
    answers: List[AnswerOption] = [answer1, AnswerOption(), AnswerOption(), AnswerOption()]
    return Question(text, answers)

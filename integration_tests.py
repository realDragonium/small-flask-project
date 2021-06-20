import time
import unittest

from quiz.StorageRepository import StorageRepository
from quiz.test_quiz_controller import TestQuizController
from sql.SQLStorageRepository import SQLStorageRepository


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Timeout so the database has some time to start up when running test in container
    time.sleep(5)

    repo: StorageRepository = SQLStorageRepository()

    test_names = loader.getTestCaseNames(TestQuizController)
    for name in test_names:
        suite.addTest(TestQuizController(name, repo))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)



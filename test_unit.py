import unittest

from quiz.CacheStorageRepository import CacheStorageRepository
from quiz.StorageRepository import StorageRepository
from quiz.test_quiz_controller import TestQuizController

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    repo: StorageRepository = CacheStorageRepository()

    test_names = loader.getTestCaseNames(TestQuizController)
    for name in test_names:
        suite.addTest(TestQuizController(name, repo))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)



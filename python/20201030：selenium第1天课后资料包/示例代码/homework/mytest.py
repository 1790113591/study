import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        print("\nsetUp ...")

    def tearDown(self):
        print("tearDown...\n")

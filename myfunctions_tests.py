import unittest
from random import randint
from my_modules.string_checkers.substring_checker import substring_checker \
    as check_str


class CheckStrTests(unittest.TestCase):

    def test_regression(self):
        self.assertTrue(check_str("12345", "45"))
        self.assertFalse(check_str("12345", "54"))

    def test_long_strings(self):
        x = ""
        y = ""
        for i in range(1000000):
            x += str(randint(0, 9))
        for i in range(10):
            y += str(randint(0, 9))

        self.assertEqual(check_str(x, y), y in x)
        self.assertEqual(check_str(y, x), x in y)

    def test_empty_string(self):
        empty = ""
        not_empty = "hello"
        self.assertEqual(check_str(empty, not_empty), not_empty in empty)
        self.assertEqual(check_str(not_empty, empty), empty in not_empty)
        self.assertEqual(check_str(empty, empty), empty in empty)

    def test_random(self):
        try:
            for i in range(1000):
                x = str(randint(0, 1000000))
                y = str((randint(0, 100)))
                self.assertEqual(check_str(x, y), y in x)
        except AssertionError:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

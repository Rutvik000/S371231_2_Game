'''import unittest'''
import unittest
from game import GuessTheNumber


class TestGuessTheNumberGame(unittest.TestCase):
    """
    This class is for unittest TestGuessTheNumberGame.
    """

    def test_generate_random_number(self):
        """
        Test the generate_random_number method.
        """
        game = GuessTheNumber()
        number = game.generate_random_number()
        self.assertIsInstance(number, int)
        self.assertGreaterEqual(number, 0)
        self.assertLessEqual(number, 9999)

    def test_check_guess(self):
        """
        Test the check_guess method.
        """
        game = GuessTheNumber()
        game.random_number = 1234
        self.assertEqual(game.check_guess(1234), "0000")
        self.assertEqual(game.check_guess(5678), "----")
        self.assertEqual(game.check_guess(1243), "00XX")
        self.assertEqual(game.check_guess(1324), "0XX0")
        self.assertEqual(game.check_guess(3421), "XXXX")
        self.assertEqual(game.check_guess(1231), "000X")


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from codealpha.hangman import WORDS, MAX_WRONG_GUESSES


class HangmanTests(unittest.TestCase):
    def test_word_bank_is_available(self):
        self.assertGreaterEqual(len(WORDS), 5)
        self.assertTrue(all(word.isalpha() and word.isupper() for word in WORDS))

    def test_wrong_guess_limit(self):
        self.assertEqual(MAX_WRONG_GUESSES, 6)


if __name__ == "__main__":
    unittest.main()

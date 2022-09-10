import unittest
import hangman


class TestHangman(unittest.TestCase):
    def test_guess_next_letter(self):
        pattern = "____e"
        used_letters = list("abcde")
        word_list = ['about', 'abcde', 'isnot']
        res = hangman.guess_next_letter(pattern, used_letters, word_list)
        self.assertEqual(res, ['abcde'])
        print(res)


if __name__ == '__main__':
    print(TestHangman.test_guess_next_letter())

import unittest
from input_handler import yes_no, get_number_input, get_string
from unittest.mock import patch

class InputHandlerTests(unittest.TestCase):
    def test_yes_no(self):
        # Testing a single valid negative input
        with patch('builtins.input', side_effect='no'):
            result = yes_no('')
            self.assertEqual(result, False)

        # Testing a single valid negative input, with a space
        with patch('builtins.input', side_effect=' n'):
            result = yes_no('')
            self.assertEqual(result, False)

        # Single uppercase negative input, with space
        with patch('builtins.input', side_effect='NO '):
            result = yes_no('')
            self.assertEqual(result, False)

        # Single positive input
        with patch('builtins.input', side_effect='y'):
            result = yes_no('')
            self.assertEqual(result, True)

        # Single mixed-case positive input
        with patch('builtins.input', side_effect=' YeS ') as m:
            result = yes_no('')
            self.assertEqual(result, True)

        # Multiple inputs, return the first valid one
        with patch('builtins.input', side_effect=['a', 'b', 'yes', 'no']) as m:
            result = yes_no('')
            self.assertEqual(result, True)
        with patch('builtins.input', side_effect=['no', 'hello', 'y']) as m:
            result = yes_no('')
            self.assertEqual(result, False)

    def test_get_number_input(self):
        # single valid number
        with patch('builtins.input', side_effect='3'):
            result = get_number_input(2,5)
            self.assertEqual(result, 3)

        # single valid number with space
        with patch('builtins.input', side_effect=' 4   '):
            result = get_number_input(2,5)
            self.assertEqual(result, 4)

        # multiple inputs, return first valid one
        with patch('builtins.input', side_effect=['1','6','2','5','3']):
            result = get_number_input(2,5)
            self.assertEqual(result, 2)

    def test_get_string(self):
        with patch('builtins.input', side_effect=['', ' ', ' hello', ' hey']):
            result = get_string('')
            self.assertEqual(result, 'hello')


if __name__ == '__main__':
    unittest.main()

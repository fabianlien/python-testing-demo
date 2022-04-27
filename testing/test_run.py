import unittest
from run import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_throws_error_if_value_passed_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_throws_error_if_list_passed_is_empty(self):
        self.assertRaises(ValueError,  even_number_of_evens, [])

    def test_values_in_list(self):
        self.assertTrue(even_number_of_evens([2, 4]))
        self.assertFalse(even_number_of_evens([2]))
        self.assertFalse(even_number_of_evens([1, 3]))


if __name__ == '__main__':
    unittest.main()

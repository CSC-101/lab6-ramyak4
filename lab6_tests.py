import data
import lab6
import unittest
from data import Book


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books(self):
        input = [Book(["J.K. Rowling"], "Harry Potter"),
                 Book(["Rick Riordan"],"Percy Jackson"),
                 Book(["Suzanne Collins"], "Hunger Games"),
                 Book( ["Veronica Roth"],"Divergent")]
        expected = [Book( ["Veronica Roth"],"Divergent"),
                    Book(["J.K. Rowling"], "Harry Potter"),
                    Book(["Suzanne Collins"], "Hunger Games"),
                    Book(["Rick Riordan"],"Percy Jackson")]
        self.assertEqual(expected, lab6.selection_sort_books(input))

    def test_selection_sort_books2(self):
        input = [Book(["Marie Lu"], "Legend"),
                 Book(["Sabaa Tahir"],"Ember in the Ashes"),
                 Book(["Victoria Aveyard"], "Red Queen"),
                 Book( ["Rebecca Yarros"],"Fourth Wing")]
        expected = [Book(["Sabaa Tahir"],"Ember in the Ashes"),
                    Book(["Rebecca Yarros"],"Fourth Wing"),
                    Book(["Marie Lu"], "Legend"),
                    Book( ["Victoria Aveyard"], "Red Queen")]
        self.assertEqual(expected, lab6.selection_sort_books(input))

    # Part 2
    def test_swap_case(self):
        input = "BeaUtiFul"
        expected = "bEAuTIfUL"
        self.assertEqual(expected, lab6.swap_case(input))

    def test_swap_case2(self):
        input = "quirky"
        expected = "QUIRKY"
        self.assertEqual(expected, lab6.swap_case(input))

    # Part 3
    def test_str_translate(self):
        input = "banana"
        expected = "barara"
        self.assertEqual(expected, lab6.str_translate(input, 'n', 'r'))

    def test_str_translate2(self):
        input = "Caterpillar"
        expected = "Catewpillaw"
        self.assertEqual(expected, lab6.str_translate(input, 'r', 'w'))

    # Part 4
    def test_histogram(self):
        input = "I am so smart like really really smart"
        expected = {'I': 1, 'am': 1, 'so': 1, 'smart': 2, 'like': 1, 'really': 2}
        self.assertEqual(expected, lab6.histogram(input))
    def test_histogram2(self):
        input = "hi hello hello bye bye bye"
        expected = {'hi': 1, 'hello': 2, 'bye': 3}
        self.assertEqual(expected, lab6.histogram(input))

if __name__ == '__main__':
    unittest.main()

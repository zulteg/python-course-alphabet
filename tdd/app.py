import random
import unittest
import string


def get_random_list():
    return [random.randint(0, 100) for _ in range(20)]


class TestGetRandomList(unittest.TestCase):
    """
    1. type of return type
    2. elements count
    3. type of elements in list
    4. value of elements in list
    """

    def test_return_type(self):
        self.assertIsInstance(get_random_list(), list)

    def test_elements_count(self):
        self.assertEqual(len(get_random_list()), 20)

    def test_elements_type(self):
        for element in get_random_list():
            self.assertIsInstance(element, int)

    def test_elements_value(self):
        for element in get_random_list():
            self.assertTrue(0 <= element <= 100)


def get_list_of_chars():
    """
    list of dict with one {key: value}
    key -> char
    value -> number of char
    """
    return [{char: pos + 1} for pos, char
            in enumerate(string.ascii_lowercase)]
    # return [{'a': 1}, None, False, {'c': 3}, {'d': 4}, {'e': 5}, {'f': 6},
    #         {'g': 7}, {'h': 8}, {'i': 9}, {'j': 10}, {'k': 11}, {'l': 12},
    #         {'m': 13}, {'n': 14}, {'o': 15}, {'p': 16}, {'q': 17}, {'r': 18},
    #         {'s': 19}, {'t': 20}, {'u': 21}, {'v': 22}, {'w': 23}, {'x': 24},
    #         {'y': 25}, {'z': 26}]
    # return [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}, {'e': 5}, {'f': 6},
    #         {'g': 7}, {'h': 8}, {'i': 9}, {'j': 10}, {'k': 11}, {'l': 12},
    #         {'m': 13}, {'n': 14}, {'o': 15}, {'p': 16}, {'q': 17}, {'r': 18},
    #         {'s': 19}, {'t': 20}, {'u': 21}, {'v': 22}, {'w': 23}, {'x': 24},
    #         {'y': 25}, {'z': 26}]
    # return []


class TestGetListOfChart(unittest.TestCase):
    """
    1. type of return value
    2. elements count
    3. type of elements in list
    4. value of elements in list
    5. test dict keys count
    """
    expected_result = [
        {'a': 1}, {'b': 2}, {'c': 3}, {'d': 4},
        {'e': 5}, {'f': 6}, {'g': 7}, {'h': 8},
        {'i': 9}, {'j': 10}, {'k': 11}, {'l': 12},
        {'m': 13}, {'n': 14}, {'o': 15}, {'p': 16},
        {'q': 17}, {'r': 18}, {'s': 19}, {'t': 20},
        {'u': 21}, {'v': 22}, {'w': 23}, {'x': 24},
        {'y': 25}, {'z': 26}
    ]

    def test_return_type(self):
        self.assertIsInstance(get_list_of_chars(), list)

    def test_elements_count(self):
        self.assertEqual(len(get_list_of_chars()), len(self.expected_result))

    def test_elements_type(self):
        actual_result = get_list_of_chars()
        self.assertTrue(actual_result)

        for element in actual_result:
            self.assertIsInstance(element, dict)

    def test_elements_value(self):
        actual_result = get_list_of_chars()
        self.assertTrue(actual_result)

        self.assertListEqual(actual_result, self.expected_result)




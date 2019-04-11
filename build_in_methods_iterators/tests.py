import random
import unittest

from build_in_methods_iterators.solved_homework import (
    task_4_min_value_integers,
    task_5_min_value_strings,
    task_6_min_value_list_of_dicts,
    task_9_reduce_min_value
)


class SumTestCases(unittest.TestCase):

    def test_empty(self):
        pass


class MinTestCases(unittest.TestCase):

    def test_task_4_valid_values(self):
        self.assertEqual(task_4_min_value_integers([1, 29, 5, 9]), 1)

        for i in range(1, 20):
            given_data = [random.randint(-100, 100) for _ in range(i)]
            actual_result = task_4_min_value_integers(given_data)
            given_data.sort()
            self.assertEqual(actual_result, given_data[0])

    def test_task_4_empty_list(self):
        self.assertIsNone(task_4_min_value_integers([]))

    def test_task_4_duplicate_values(self):
        given_data = [1, 2, 3, 8, 10, 12, 12, 23, 23, 1, 1, 2]
        self.assertEqual(task_4_min_value_integers(given_data), 1)

    def test_task_5_valid_value(self):
        given_data = "So the normal way you might go about doing this task in python is using a basic for loop:".split()
        self.assertEqual(task_5_min_value_strings(given_data), 'a')

    def test_task_5_empty_list(self):
        self.assertIsNone(task_5_min_value_strings([]))

    def test_task_5_int_values(self):
        given_data = ['Year', 'has', 12, 'months']
        self.assertEqual(task_5_min_value_strings(given_data), "12")

    def test_task_6_valid_values(self):
        members = [
            {'age': 43, 'name': 'Denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'Spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'Claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'Homer'}
        ]
        self.assertDictEqual(task_6_min_value_list_of_dicts(data=members, key='age'), members[4])

    def test_task_6_empty_fields(self):
        members = [
            {'age': 43, 'name': 'Denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'Spike'},
            {'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'Claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'Homer'}
        ]
        self.assertDictEqual(task_6_min_value_list_of_dicts(data=members, key='age'), members[2])



class MaxTestCases(unittest.TestCase):

    def test_task_7_valid_values(self):
        pass


class ListComprehensionCases(unittest.TestCase):

    def test_empty(self):
        pass


class DictComprehension(unittest.TestCase):

    def test_empty(self):
        pass


class GeneratorComprehensions(unittest.TestCase):

    def test_empty(self):
        pass


class GeneratorTestCases(unittest.TestCase):

    def test_empty(self):
        pass


class FilterTestCases(unittest.TestCase):

    def test_empty(self):
        pass


if __name__ == "__main__":
    unittest.main()
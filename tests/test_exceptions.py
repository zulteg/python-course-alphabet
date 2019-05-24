import unittest


def division(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Second argument should not be zero")
    return a / b


class TestException(unittest.TestCase):

    def test_exception_raise(self):
        with self.assertRaises(ValueError) as context:
            division(10, 0)
        self.assertTrue("Second argument should not be zero" in context.exception.args)

    def test_valid_data(self):
        actual_result = division(10, 2)
        expected_result = 5.0
        self.assertIsInstance(actual_result, float)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()

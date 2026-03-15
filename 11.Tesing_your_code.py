# ------------------ Code To Be Tested ------------------

def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def get_full_name(first, last, middle=""):
    if middle:
        return f"{first} {middle} {last}".title()
    return f"{first} {last}".title()


# ------------------ Import Testing Framework ------------------

import unittest


# ------------------ Basic Test Structure ------------------
class TestMathFunctions(unittest.TestCase):

    # Simple equality test
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    # Testing multiple assertions
    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertNotEqual(divide(10, 2), 3)
        self.assertTrue(divide(9, 3) == 3)


# ------------------ Using setUp() ------------------
class TestNameFunction(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.first = "john"
        self.middle = "fitzgerald"
        self.last = "kennedy"

    def test_first_last_name(self):
        name = get_full_name(self.first, self.last)
        self.assertEqual(name, "John Kennedy")

    def test_first_middle_last_name(self):
        name = get_full_name(self.first, self.last, self.middle)
        self.assertEqual(name, "John Fitzgerald Kennedy")


# ------------------ Testing Exceptions ------------------
class TestExceptions(unittest.TestCase):

    def test_divide_by_zero(self):
        """Check that ZeroDivisionError is raised"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


# ------------------ Running Tests ------------------
if __name__ == "__main__":
    unittest.main()
import unittest
from app import greet
class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from FirstName LastName!")


if _name_ == "_main_":
    unittest.main()
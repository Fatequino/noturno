import unittest
from unittest import result
import my_flask_app

class TestClass(unittest.TestCase):

    def test_home(self):
        return my_flask_app.home

    def test_remove_acentos(self):
        self.assertTrue(my_flask_app.remove_acentos("é") == "e")

if __name__ == '__main__':
    unittest.main()
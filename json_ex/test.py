
import unittest
import json
import serialization

class TestSerialization(unittest.TestCase):

    def test_load(self):
        reader = serialization.FileReader()
        file = open("sample.json", "r")
        dictionary = json.load(file)
        self.assertTrue(dictionary["Lisa"] == 123)

if __name__ == '__main__':
    unittest.main()

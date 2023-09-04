import unittest
from examples.common_api import gram_to_kilogram, kilogram_to_gram
import logging


#
class Test(unittest.TestCase):
    def test_gram_to_kilogram(self):
        self.assertEqual(gram_to_kilogram(1000), 1)

    def test_kilogram_to_gram(self):
        self.assertEqual(kilogram_to_gram(1), 1000)

    def test_ui_class(self):
        from examples.ui_class import show_ui

        self.assertEqual(show_ui(1000), True)

    def test_gram_to_kilogram_dict_type(self):
        with self.assertRaises(TypeError):
            gram_to_kilogram({"a": 1, "b": 2})

    def test_gram_to_kilogram_list_type(self):
        with self.assertRaises(TypeError):
            gram_to_kilogram([1, 2, 3])

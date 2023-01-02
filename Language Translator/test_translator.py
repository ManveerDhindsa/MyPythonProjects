import unittest
from translator import english_to_french, english_to_german

class EnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Bye'), 'Bonjour')

class EnglishToGerman(unittest.TestCase):
    def test_english_to_german(self):
        self.assertEqual(english_to_german(' '),' ')
        self.assertEqual(english_to_german('Hello'), 'Hallo')
        self.assertNotEqual(english_to_german('Bye'), 'Bonjour')

unittest.main()
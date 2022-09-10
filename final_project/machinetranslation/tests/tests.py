import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        # Checking for null input
        self.assertEqual(english_to_french(""), "")
        
        # checking translation for hello
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        # Checking for null input
        self.assertEqual(french_to_english(""), "")

        # checking translation for bonjour
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
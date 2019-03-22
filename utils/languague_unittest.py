import unittest
from language import language

class TestLanguage(unittest.TestCase):

    def test_check_select(self):
        language_ = language.Languague()
        self.assertIn("a", language_.list_key_words)



if __name__ == "__main__":
    unittest.main()

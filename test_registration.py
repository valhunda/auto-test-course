import unittest
from helpful_functions import checking_registration


class TestRegistration(unittest.TestCase):
    def test_correct_registration(self):
        registration_text = checking_registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(registration_text, "Congratulations! You have successfully registered!",
                         "Expected massage does not match the actual massage")

    def test_wrong_registration(self):
        registration_text = checking_registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(registration_text, "Congratulations! You have successfully registered!",
                         "Expected massage does not match the actual massage")


if __name__ == "__main__":
    unittest.main()

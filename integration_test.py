import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_calculator_page_contains_heading(self):
        response = self.client.get("/")
        self.assertIn(b"Calculator", response.data)

if __name__ == "__main__":
    unittest.main()

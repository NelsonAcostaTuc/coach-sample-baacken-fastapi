
import unittest
from fastapi.testclient import TestClient
from api.main import app

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "The healt check is successful!")

    def test_read_cars(self):
        response = self.client.get("/cars")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_car(self):
        car_data = {
            "brand": "Test Brand",
            "model": "Test Model",
            "year": 2020,
            "subsidiary_id": 1
        }
        response = self.client.post("/cars", json=car_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["brand"], "Test Brand")
        self.assertEqual(response.json()["model"], "Test Model")

if __name__ == "__main__":
    unittest.main()
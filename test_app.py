import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_predict(self):
        result = self.app.post('/predict', data=dict(MedInc=3.5, HouseAge=20, AveRooms=5))
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()

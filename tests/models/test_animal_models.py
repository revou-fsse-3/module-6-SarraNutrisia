import unittest
from app.models.animal import Animals

class TestAnimalsModel(unittest.TestCase):
    def setUp(self):
        self.animal = Animals(
            species='Tiger',
            age='5 years',
            gender='Male',
            special_requirements='None'
        )

    def test_as_dict(self):
        expected_result = {
            "id": None,  # The id will be None until it's assigned in the database
            "species": 'Tiger',
            "age": '5 years',
            "gender": 'Male',
            "special_requirements": 'None'
        }
        self.assertEqual(self.animal.as_dict(), expected_result)

    def test_as_dict_with_id(self):
        # If the id is assigned (not None), it should be included in the dictionary
        self.animal.id = 1
        expected_result_with_id = {
            "id": 1,
            "species": 'Tiger',
            "age": '5 years',
            "gender": 'Male',
            "special_requirements": 'None'
        }
        self.assertEqual(self.animal.as_dict(), expected_result_with_id)

if __name__ == '__main__':
    unittest.main()

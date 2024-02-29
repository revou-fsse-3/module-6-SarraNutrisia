import unittest
from app.models.employee import Employees

class TestEmployeesModel(unittest.TestCase):
    def setUp(self):
        self.employee = Employees(
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            role='Manager',
            schedule='Monday-Friday'
        )

    def test_as_dict(self):
        expected_result = {
            "id": None,  # The id will be None until it's assigned in the database
            "name": 'John Doe',
            "email": 'john@example.com',
            "phone_number": '1234567890',
            "role": 'Manager',
            "schedule": 'Monday-Friday'
        }
        self.assertEqual(self.employee.as_dict(), expected_result)

    def test_as_dict_with_id(self):
        # If the id is assigned (not None), it should be included in the dictionary
        self.employee.id = 1
        expected_result_with_id = {
            "id": 1,
            "name": 'John Doe',
            "email": 'john@example.com',
            "phone_number": '1234567890',
            "role": 'Manager',
            "schedule": 'Monday-Friday'
        }
        self.assertEqual(self.employee.as_dict(), expected_result_with_id)

if __name__ == '__main__':
    unittest.main()

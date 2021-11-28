import unittest
from person_1 import Person


class TestPerson(unittest.TestCase):
    def test_get_phone(self):
        expected_phone = 12345
        test_person = Person('Oleg', 'Levitskiy', expected_phone)
        actual_phone = test_person.get_phone()
        self.assertEqual(actual_phone, expected_phone, 'ОПАНА')


if __name__ == '__main__':
    unittest.main()

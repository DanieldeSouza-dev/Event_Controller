# Zona de importações

import unittest
from src.models.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff(3, 'Daniel Souza', '29061504')

    def test_id_is_correctly(self):
        self.assertEqual(self.staff.id, 3)

    def test_name_is_set_correctly(self):
        self.assertEqual(self.staff.name, 'Daniel Souza')

    def test_password_is_hashed(self):
        hashed = self.staff.to_dict()['password_hash']
        print('HASHED', hashed)
        self.assertNotEqual(hashed, '29061504')
        self.assertTrue(hashed.startswith('$pbkdf2-sha256$'))

    def test_to_dict_structure(self):
        result = self.staff.to_dict()
        print(result)
        self.assertIn('id', result)
        self.assertIn('name', result)
        self.assertIn('password_hash', result)
        self.assertIn('is_staff', result)

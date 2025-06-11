# Zona de importações

import unittest
from src.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
            self.user = User(2, 'Maria', '123456')

    def test_id_is_correctly(self):
        self.assertEqual(self.user.id, 2)

    def test_name_is_set_correctly(self):
        self.assertEqual(self.user.name, 'Maria')

    def test_password_is_hashed(self):
        hashed = self.user.to_dict()['password_hash']
        print('HASHED:', hashed)
        self.assertNotEqual(hashed, '123456')
        self.assertTrue(hashed.startswith('$pbkdf2-sha256$'))

    def test_to_dict_structure(self):
        result = self.user.to_dict()
        print(result)
        self.assertIn('id', result)
        self.assertIn('name', result)
        self.assertIn('password_hash', result)
        self.assertIn('is_staff', result)
        self.assertFalse(result['is_staff'])

    def test_favourites_is_list(self):
        self.assertTrue(hasattr(self.user, 'favorites'))
        self.assertIsInstance(self.user.favorites, list)

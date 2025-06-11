# Zona de importação

import unittest #importação necessária para os testes
from src.models.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person(1, 'Daniel', '123456')

    def test_id_is_correctly(self):
        self.assertEqual(self.person.id, 1)

    def test_name_is_set_correctly(self):
        self.assertEqual(self.person.name, 'Daniel')

    def test_password_is_hashed(self):
        hashed = self.person.to_dict()['password_hash']
        print('HASHED', hashed)
        self.assertNotEqual(hashed, '123456')
        self.assertTrue(hashed.startswith('$pbkdf2-sha256$'))

    def test_to_dict_structure(self):
        result =self.person.to_dict()
        print(result)
        self.assertIn('id', result)
        self.assertIn('name', result)
        self.assertIn('password_hash', result)

# Zona de importações

import unittest
from src.models.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff(3, 'Daniel Souza', '29061504', 'daniel@gmail.com', '529.982.247-25')

    def test_id_is_correctly(self):
        self.assertEqual(self.staff.id, 3)

    def test_name_is_set_correctly(self):
        self.assertEqual(self.staff.name, 'Daniel Souza')

    def test_email_is_set_correctly(self):
        self.assertEqual(self.staff.email, 'daniel@gmail.com')

    def test_cpf_is_clean(self):
        self.assertEqual(self.staff.cpf, '52998224725')

    def test_masked_cpf_is_correct(self):
        self.assertEqual(self.staff.masked_cpf, '***.982.247-**')

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
        self.assertIn('email', result)
        self.assertIn('cpf', result)
        self.assertIn('password_hash', result)
        self.assertIn('is_staff', result)

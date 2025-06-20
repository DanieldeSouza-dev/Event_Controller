# Zona de importações

import unittest
from datetime import datetime
from src.models.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff(3, 'Daniel Souza', 'daniel@gmail.com', '529.982.247-25', '29061504')

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

    # Teste de funcionalidade (criação)

    def test_register_user_creates_user_correctly(self):
        user_data = {
            'id': 4,
            'name': 'Juliano',
            'email': 'juliano@gmail.com',
            'cpf': '012.345.678-90',
            'password': 'password123'
        }
        new_user = self.staff.register_user(user_data)
        self.assertEqual(new_user.id, 4)
        self.assertEqual(new_user.name, 'Juliano')
        self.assertEqual(new_user.email, 'juliano@gmail.com')
        self.assertEqual(new_user.cpf, '01234567890')
        self.assertTrue(new_user.verify_password('password123'))
        print('\nNew user created: ', new_user.to_dict())
        self.assertTrue(True)

    def test_register_staff_creates_staff_correctly(self):
        staff_data = {
            'id': 5,
            'name': 'Danilo',
            'email': 'danilo@gmail.com',
            'cpf': '577.569.125-35',
            'password': 'senha12345'
        }
        new_staff = self.staff.register_staff(staff_data)
        self.assertEqual(new_staff.id, 5)
        self.assertEqual(new_staff.name, 'Danilo')
        self.assertEqual(new_staff.email, 'danilo@gmail.com')
        self.assertEqual(new_staff.cpf, '57756912535')
        self.assertTrue(new_staff.verify_password('senha12345'))
        print('\nNew staff created: ', new_staff.to_dict())
        self.assertTrue(True)

    def test_register_show_creates_show_correctly(self):
        show_data = {
            'id': 6,
            'name': 'Viradão',
            'date': '2025-06-21'
        }
        new_show = self.staff.register_show(show_data)
        self.assertEqual(new_show.show_id, 6)
        self.assertEqual(new_show.name, 'Viradão')
        self.assertEqual(new_show.date, datetime(2025, 6, 21))
        print('\nShow created: ', new_show.to_dict())
        self.assertTrue(True)

    # Teste de funcionalidade (update)

    def test_update_user_name(self):
        user_data = {
            'id': 7,
            'name': 'João',
            'email': 'joao@gmail.com',
            'cpf': '781.789.715-85',
            'password': '87620583'
        }
        user = self.staff.register_user(user_data)
        self.staff.update_user_name(user, 'Nascimento')
        self.assertEqual(user.name, 'Nascimento')
        print('\nNew user name: ', user.to_dict())
        self.assertTrue(True)

    def test_update_user_password(self):
        user_data = {
            'id': 8,
            'name': 'Julia',
            'email': 'julia@gmail.com',
            'cpf': '960.807.595-51',
            'password': 'teste123456'
        }
        user = self.staff.register_user(user_data)
        self.staff.update_user_password(user, 'novasenha123456')
        self.assertTrue(user.verify_password('novasenha123456'))

    # Still in progress:
    
    """def tes_update_staff_name(self):
    def test_update_staff_password(self):
    
    # Teste de funcionalidade (delete)

    def test_delete_user(self):
    def test_delete_staff(self):
    def test_delete_show(self):"""
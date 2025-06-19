# Zona de importação

import unittest #importação necessária para os testes
from src.models.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person(1, 'Daniel', '123456', 'daniel@gmail.com', '529.982.247-25')

    # Testes
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

    def test_verify_password_correct(self):
        self.assertTrue(self.person.verify_password('123456'))

    def test_verify_password_incorrect(self):
        self.assertFalse(self.person.verify_password('qwerty'))

    def test_update_name(self):
        self.person.update_name('Ayrton')
        self.assertEqual(self.person.name, 'Ayrton')

    def test_update_password(self):
        self.person.update_password('135790')
        self.assertTrue(self.person.verify_password('135790'))

    def test_verify_masked_cpf(self):
        self.assertEqual(self.person.masked_cpf, '***.982.247-**')
    

    # Teste para resultados invalidos:
    def test_invalid_id_raises(self):
        with self.assertRaises(ValueError):
            Person(-1, 'Jonas', 'senha123', 'j@j.com', '529.982.247-25')

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            Person(2, '', 'senha123', 'j@j.com', '529.982.247-25')

    def test_invalid_password_raises(self):
        with self.assertRaises(ValueError):
            Person(3, 'Jonas', '123', 'j@j.com', '529.982.247-25')

    def test_invalid_email_raises(self):
        with self.assertRaises(ValueError):
            Person(4, 'Jonas', 'senha123', '', '529.982.247-25')
    
    def test_invalid_cpf_raises(self):
        with self.assertRaises(ValueError):
            Person(5, 'Jonas', 'senha123', 'j@j.com', '1111111122222')

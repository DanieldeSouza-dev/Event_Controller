# Zona de importações

import unittest
from src.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
            self.user = User(2, 'Maria', '123456', 'maria@gmail.com', '529.982.247-25')

    def test_id_is_correctly(self):
        self.assertEqual(self.user.id, 2)

    def test_name_is_set_correctly(self):
        self.assertEqual(self.user.name, 'Maria')

    def test_password_is_hashed(self):
        hashed = self.user.to_dict()['password_hash']
        print('HASHED:', hashed)
        self.assertNotEqual(hashed, '123456')
        self.assertTrue(hashed.startswith('$pbkdf2-sha256$'))

    def test_email_is_set_correctly(self):
        self.assertEqual(self.user.email, 'maria@gmail.com')

    def test_cpf_is_clean(self):
        self.assertEqual(self.user.cpf, '52998224725')

    def test_masked_cpf_is_correct(self):
        self.assertEqual(self.user.masked_cpf, '***.982.247-**')

    def test_to_dict_structure(self):
        result = self.user.to_dict()
        print(result)
        self.assertIn('id', result)
        self.assertIn('name', result)
        self.assertIn('password_hash', result)
        self.assertIn('email', result)
        self.assertIn('cpf', result)
        self.assertIn('is_staff', result)
        self.assertFalse(result['is_staff'])

    def test_favourites_is_list(self):
        self.assertTrue(hasattr(self.user, 'favorites'))
        self.assertIsInstance(self.user.favorites, list)

    def test_add_favorites_adds_unique(self):
        self.user.add_favorites(101)
        self.assertIn(101, self.user.favorites)
        self.user.add_favorites(101) # Adicionando um duplicado
        self.assertEqual(self.user.favorites.count(101), 1)

    def test_remove_favorites_removes_existing(self): # Remove um existente
        self.user.add_favorites(202)
        self.user.remove_favorites(202)
        self.assertNotIn(202, self.user.favorites)

    def test_remove_favorites_does_nothing_if_not_existing(self): # Tenta remover um que não existe
        self.user.remove_favorites(999)
        self.assertEqual(self.user.favorites, [])

    def test_from_dict_recreates_user(self):
        original = User(3, 'Italo', 'senha123', 'i@gmail.com', '529.982.247-25')
        original.add_favorites(111)
        original.add_favorites(222)
        user_dict = original.to_dict()
        recreated = User.from_dict(user_dict)
        self.assertEqual(recreated.id, original.id)
        self.assertEqual(recreated.name, original.name)
        self.assertEqual(recreated.email, original.email)
        self.assertEqual(recreated.favorites, [111, 222])
        print(recreated.to_dict())
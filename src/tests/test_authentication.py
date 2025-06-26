# Zona de importações

import unittest
from src.models.user import User
from src.models.staff import Staff
from src.core.authentication import authenticate_staff, authenticate_user

class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.user = User(1, 'Daniel', 'daniel@gmail.com', '158.176.150-37', 'senha1234')
        self.staff = Staff(2, 'Alana', 'alana@gmail.com', '979.344.590-41', 'senha123456')
        self.users = [self.user]
        self.staffs = [self.staff]


    # Teste com sucesso
    def test_authentication_user_success(self):
        result = authenticate_user(1, 'senha1234', self.users)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'Daniel')
        print(result)

    def test_authentication_staff_success(self):
        result = authenticate_staff(2, 'senha123456', self.staffs)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'Alana')
        print(result)

    # Teste com falha (id)
    def test_authenticate_user_failure_wrong_id(self):
        result = authenticate_user(999, 'senha1234', self.users)
        self.assertIsNone(result)

    def test_authenticate_staff_failure_wrong_id(self):
        result = authenticate_staff(888, 'senha123456', self.staffs)
        self.assertIsNone(result)

    #Teste com falha (senha)
    def test_authenticate_user_failure_wrong_password(self):
        result = authenticate_user(1, 'senhaErrada1', self.users)
        self.assertIsNone(result)

    def test_authenticate_staff_failure_wrong_password(self):
        result = authenticate_staff(2, 'senhaErrada2', self.staffs)
        self.assertIsNone(result)
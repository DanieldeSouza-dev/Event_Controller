# Zona de importações

import unittest
from datetime import datetime
from src.models.user import User
from src.models.staff import Staff
from src.models.shows import Show
from src.core.system import SystemController

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.user = User(1, 'Daniel', 'daniel@gmail.com', '374.666.170-69', 'senha1234')
        self.staff = Staff(2, 'Junior', 'juninho@gmail.com', '695.387.420-10', 'senha1234567')
        self.shows = Show(11, datetime(2025, 6, 24), '10 Horas de arrocha')
        
        self.users = [self.user]
        self.staffs = [self.staff]
        self.shows = [self.shows]

        self.system = SystemController(self.users, self.staffs, self.shows)

    # Testes de login
    def test_login_user_success(self):
        result = self.system.login_user(1, 'senha1234')
        self.assertTrue(result)
        print(result)

    def test_login_staff_success(self):
        result = self.system.login_staff(2, 'senha1234567')
        self.assertTrue(result)
        print(result)

    # Falha no login
    def test_login_user_failure(self):
        result = self.system.login_user(1, 'senhaErrada1')
        self.assertFalse(result)

    def test_login_staff_failure(self):
        result = self.system.login_staff(2, 'senhaErrada2')
        self.assertFalse(result)

    # Testes de estado atual
    def test_get_logged_user_returns_user(self):
        self.system.login_user(1, 'senha1234')
        result = self.system.get_logged_user()
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'Daniel')

    def test_get_logged_staff_returns_staff(self):
        self.system.login_staff(2, 'senha1234567')
        result = self.system.get_logged_staff()
        self.assertIsNotNone(result)
        self.assertEqual(result.name, 'Junior')
        
     # Testes de Loggout
    def test_logout_clears_current_staff_and_user(self):
        # Login User e verificação
        self.system.login_user(1, 'senha1234')
        self.assertIsNotNone(self.system.get_logged_user())

        #Login Staff e verificação
        self.system.login_staff(2, 'senha1234567')
        self.assertIsNotNone(self.system.get_logged_staff())

        # Loggout
        self.system.loggout()

        # Verificação de Loggout
        self.assertIsNone(self.system.get_logged_user())
        self.assertIsNone(self.system.get_logged_staff())

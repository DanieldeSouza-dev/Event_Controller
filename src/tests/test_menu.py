# Zona de importação

import unittest
from unittest.mock import patch, MagicMock
from src.interface.menu import Interface
from src.core.system import SystemController

class TestMenu(unittest.TestCase):
    def setUp(self):
        # Cria uma instancia do SystemController com listar para não depender de dados reais
        self.system = SystemController(users = [], staff = [], show = [])
        self.interface  = Interface(self.system)

        # Cria um mockup para user o codigo real na hora de usar
        self.interface.staff_functions = MagicMock()
        self.interface.user_functions = MagicMock()

    @patch('builtins.print')
    @patch('builtins.input')
    def test_show_login_menu_invalid_input_then_exit(self, mock_input, mock_print):
        # Simula duas entradas: primeira válida e depois sair
        mock_input.side_effect = ['invalid', '0']

        with self.assertRaises(StopIteration):
            # Roda um show_login_menu que espera input continuo
            self.interface.show_login_menu()

        mock_print.assert_any_call('\033[0:31:0mInvalid input. Please enter a number.\033[0m')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_login_user_flow_success(self, mock_input, mock_print):
        # COnfigura mockup para entrada e sistema para aceitar login

        mock_input.side_effect = ['1', 'password123', '0'] #user_id, senha, sair

        self.system.login_user = MagicMock(return_value = True)

        # Roda o fluxo de login do usuário
        self.interface.login_user_flow()

        # Verifica se printou a mensagem de sucesso
        mock_print.assert_any_call('\033[0:32:0mUser logged in successfully!\033[0m')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_show_user_menu_logout(self, mock_input, mock_print):
        # Prepara usuário logado
        user_mock = MagicMock()
        user_mock.name = 'TestUser'
        self.system.current_user = user_mock

        # Mocka inputs para navegar
        mock_input.side_effect = ['5', '']

        # Mocka user_functions.logout_user para garantir chamada
        self.interface.user_functions.logout_user = MagicMock()

        self.interface.show_user_menu()

        # Verifica logout chamado
        self.interface.user_functions.logout_user.assert_called_once()
        mock_print.assert_any_call('\033[0:32:0mUser logged out successfully.\033[0m')

    @patch('builtins.input')
    def test_show_user_menu_exit(self, mock_input):
        user_mock = MagicMock()
        user_mock.name = 'TestUser'
        self.system.current_user = user_mock

        mock_input.side_effect = ['0']

        with self.assertRaises(SystemExit):
            self.interface.show_user_menu()


if __name__ == '__main__':
    unittest.main()
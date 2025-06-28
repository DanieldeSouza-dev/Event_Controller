# Importações de módulos
from src.core.system import SystemController
from src.core.menu_functions.staff_menu_functions import Staff_Functions
from src.core.menu_functions.user_menu_functions import User_Functions
from src.core.validators import _safe_int_input
from src.models.staff import Staff
from src.models.user import User
from src.models.shows import Show

# Importação de funcionalidade
import os
from datetime import datetime

class Interface:
    def __init__(self, system: SystemController):
        self.system = system
        self.staff_functions = Staff_Functions(self.system)
        self.user_functions = User_Functions(self.system)

    # Funções básicas
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while True:
            if self.system.get_logged_staff():
                self.show_staff_menu()
            elif self.system.get_logged_user():
                self.show_user_menu()
            else:
                self.show_login_menu()
    
    # Menu inicial
    def show_login_menu(self):
        while True:
            self.clear_screen()
            print('=== Login Menu ===')
            print('[1] Login User')
            print('[2] Login Staff')
            print('[0] Exit')
            choice = _safe_int_input('Select an option: ')

            # Validação primária de número
            if choice is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if choice == 1:
                self.login_user_flow()
            elif choice == 2:
                self.login_staff_flow()
            elif choice == 0:
                print('See you later!')
                break
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    # Menu de Login Staff
    def login_staff_flow(self):
        self.clear_screen()
        try:
            staff_id = _safe_int_input('Staff ID: ')
            if staff_id is None:
                raise ValueError ('Staff ID must be numbers.')

            password = input('Password: ')
            if self.system.login_staff(staff_id, password):
                print('\033[0:32:0mStaff logged in successfully!\033[0m')
            else:
                print('\033[0:31:0mLogin failed. Check your ID or password.\033[0m')
        except ValueError:
            print('\033[0:31:0mInvalid input. Id must be a number.\033[0m')
        input('Press Enter to continue...')

    # Menu de Login User
    def login_user_flow(self):
        self.clear_screen()
        try:
            user_id = _safe_int_input('User ID: ')
            if user_id is None:
                raise ValueError ('User ID must be numbers.')
            
            password = input('Password: ')
            if self.system.login_user(user_id, password):
                print('\033[0:32:0mUser logged in succesfully!\033[0m')
            else:
                print('\033[0:31:0mLogin failed. Please check your Id or password.\033[0m')
        except ValueError:
            print('\033[0:31:0mInvalid input. ID must be a number.\033[0m')
        input('Press Enter to continue...')

    # Menu de funcionalidade Staff
    def show_staff_menu(self):
        while True:
            self.clear_screen()
            print(f'=== Staff Menu | Logged: {self.system.get_logged_staff().name} ===')
            print('[1] Register')
            print('[2] Update')
            print('[3] Remove')
            print('[4] View')
            print('[5] Logout')
            print('[0] Exit System')
            option = _safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.show_register_menu()
            elif option == 2:
                self.show_update_menu()
            elif option == 3:
                self.show_remove_menu()
            elif option == 4:
                self.show_view_menu()
            elif option == 5:
                self.staff_functions.logout_staff()
                print('\033[0:32:0mStaff logged out successfully.\033[0m')
                input('Press Enter to continue...')
            elif option == 0:
                print("Thanks for using Event_Control. Goodbye!")
                exit()
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    # Menu de funcionalidade
    def show_register_menu(self):
        while True:
            self.clear_screen()
            print(f'=== Staff Menu | Register ===')
            print('[1] Register new user')
            print('[2] Register new staff')
            print('[3] Register new show')
            print('[0] Back')
            option = _safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.staff_functions.register_user_flow()
            elif option == 2:
                self.staff_functions.register_staff_flow()
            elif option == 3:
                self.staff_functions.register_show_flow()
            elif option == 0:
                break
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    def show_update_menu(self):
        while True:
            self.clear_screen()
            print(f'=== Staff Menu | Update ===')
            print('[1] Update user name')
            print('[2] Update user password')
            print('[3] Update staff name')
            print('[4] Update staff password')
            print('[0] Back')
            option = _safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.staff_functions.update_user_name()
            elif option == 2:
                self.staff_functions.update_user_password()
            elif option == 3:
                self.staff_functions.update_staff_name()
            elif option == 4:
                self.staff_functions.update_staff_password()
            elif option == 0:
                break
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    def show_remove_menu(self):
        while True:
            self.clear_screen()
            print(f'=== Staff Menu | Remove ===')
            print('[1] Remove user')
            print('[2] Remove staff')
            print('[3] Remove show')
            print('[0] Back')
            option = _safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.staff_functions.remove_user_flow()
            elif option == 2:
                self.staff_functions.remove_staff_flow()
            elif option == 3:
                self.staff_functions.remove_show_flow()
            elif option == 0:
                break
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    def show_view_menu(self):
        while True:
            self.clear_screen()
            print(f'=== Staff Menu | View ===')
            print('[1] View  all users')
            print('[2] View  all staffs')
            print('[3] View  all shows')
            print('[0] Back')
            option = _safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.staff_functions.view_all_users()
            elif option == 2:
                self.staff_functions.view_all_staffs()
            elif option == 3:
                self.staff_functions.view_all_shows()
            elif option == 0:
                break
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    # Menu de funcionalidade User
    def show_user_menu(self):
        while True:
            self.clear_screen()
            print(f'=== User Menu | Logged: {self.system.get_logged_user().name} ===')
            print('[1] View all shows')
            print('[2] Add show to favourite')
            print('[3] Remove show from favourite')
            print('[4] View favourite shows')
            print('[5] Logout')
            print('[0] Exit system')
            option = _safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.user_functions.view_all_shows_user()
            elif option == 2:
                self.user_functions.add_show_to_favorite()
            elif option == 3:
                self.user_functions.remove_show_from_favorite()
            elif option == 4:
                self.user_functions.view_favorite_shows()
            elif option == 5:
                self.user_functions.logout_user()
                print('\033[0:32:0mUser logged out successfully.\033[0m')
                input('Press Enter to continue...')
            elif option == 0:
                print("Thanks for using Event_Control. Goodbye!")
                exit()
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')
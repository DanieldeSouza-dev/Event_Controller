# Importações de módulos
from src.core.system import SystemController
from src.core.menu_functions.staff_menu_functions import StaffFunctions
from src.core.menu_functions.user_menu_functions import UserFunctions
from src.core.validators import safe_int_input


class Interface:
    def __init__(self, system: SystemController):
        self.system = system
        self.staff_functions = StaffFunctions(self.system)
        self.user_functions = UserFunctions(self.system)

    def run(self):
        while True:
            if self.system.get_logged_staff():
                self.show_staff_menu()
            elif self.system.get_logged_user():
                self.show_user_menu()
            else:
                should_exit = self.show_login_menu()
                if should_exit:
                    break

    # Menu inicial
    def show_login_menu(self):
        while True:
            self.system.clear_screen()
            print('=== Login Menu ===')
            print('[1] Login User')
            print('[2] Login Staff')
            print('[0] Exit')
            choice = safe_int_input('Select an option: ')

            if choice is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')

            if choice == 1:
                self.login_user_flow()
            if self.system.get_logged_user():
                break  # login bem-sucedido -> sair do loop
            elif choice == 2:
                self.login_staff_flow()
                if self.system.get_logged_staff():
                    break  # login bem-sucedido -> sair do loop
            elif choice == 0:
                print("Thanks for using Event Control. Goodbye!")
                return True
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    # Menu de Login Staff
    def login_staff_flow(self):
        self.system.clear_screen()
        try:
            staff_id = safe_int_input('Staff ID: ')
            if staff_id is None:
                raise ValueError('Staff ID must be a number.')

            password = input('Password: ')
            if self.system.login_staff(staff_id, password):
                print('\033[0:32:0mStaff logged in successfully!\033[0m')
            else:
                print('\033[0:31:0mLogin failed. Check your ID or password.\033[0m')
        except ValueError:
            print('\033[0:31:0mInvalid input. ID must be a number.\033[0m')

    # Menu de Login User

    def login_user_flow(self):
        self.system.clear_screen()
        try:
            user_id = safe_int_input('User ID: ')
            if user_id is None:
                raise ValueError('User ID must be a number.')

            password = input('Password: ')
            if self.system.login_user(user_id, password):
                print('\033[0:32:0mUser logged in successfully!\033[0m')
            else:
                print('\033[0:31:0mLogin failed. Please check your ID or password.\033[0m')
        except ValueError:
            print('\033[0:31:0mInvalid input. ID must be a number.\033[0m')

    # Menu de funcionalidade Staff
    def show_staff_menu(self):
        while True:
            self.system.clear_screen()
            logged_staff = self.system.get_logged_staff()
            print(f'=== Staff Menu | Logged: {logged_staff.name} ===')
            print('[1] Register')
            print('[2] Update')
            print('[3] Remove')
            print('[4] View')
            print('[5] Logout')
            print('[0] Exit System')
            option = safe_int_input('Select an option: ')

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
                break
            elif option == 0:
                print("Thanks for using Event Control. Goodbye!")
                exit()
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

    def show_register_menu(self):
        while True:
            self.system.clear_screen()
            print('=== Staff Menu | Register ===')
            print('[1] Register new user')
            print('[2] Register new staff')
            print('[3] Register new show')
            print('[0] Back')
            option = safe_int_input('Select an option: ')

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
            self.system.clear_screen()
            print('=== Staff Menu | Update ===')
            print('[1] Update user name')
            print('[2] Update user password')
            print('[3] Update staff name')
            print('[4] Update staff password')
            print('[0] Back')
            option = safe_int_input('Select an option: ')

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
            self.system.clear_screen()
            print('=== Staff Menu | Remove ===')
            print('[1] Remove user')
            print('[2] Remove staff')
            print('[3] Remove show')
            print('[0] Back')
            option = safe_int_input('Select an option: ')

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
            self.system.clear_screen()
            print('=== Staff Menu | View ===')
            print('[1] View all users')
            print('[2] View all staffs')
            print('[3] View all shows')
            print('[0] Back')
            option = safe_int_input('Select an option: ')

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
            self.system.clear_screen()
            logged_user = self.system.get_logged_user()
            print(f'=== User Menu | Logged: {logged_user.name} ===')
            print('[1] View all shows')
            print('[2] Add show to favourite')
            print('[3] Remove show from favourite')
            print('[4] View favourite shows')
            print('[5] Logout')
            print('[0] Exit system')
            option = safe_int_input('Select an option: ')

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
                break
            elif option == 0:
                print("Thanks for using Event Control. Goodbye!")
                exit()
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')

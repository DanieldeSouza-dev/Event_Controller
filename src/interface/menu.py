# Importações de módulos
from src.core.system import SystemController
from src.models.staff import Staff
from src.models.user import User
from src.models.shows import Show

# Importação de funcionalidade
import os
from datetime import datetime

class Interface:
    def __init__(self, system: SystemController):
        self.system = system

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

    # Valida se o número digitado era um número inteiro mesmo ou se era outra coisa
    def _safe_int_input(self, prompt: str) -> int | None:
        try:
            return int(input(prompt))
        except ValueError:
            return None
    
    # Menu inicial
    def show_login_menu(self):
        while True:
            self.clear_screen()
            print('=== Login Menu ===')
            print('[1] Login User')
            print('[2] Login Staff')
            print('[0] Exit')
            choice = self._safe_int_input('Select an option: ')

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
            staff_id = int(input('Staff ID: '))
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
            user_id = int(input('User ID: '))
            password = input('Password: ')
            if self.system.login_user(user_id, password):
                print('\033[0:32:0mUser logged in succesfully!\033[0m')
            else:
                print('\033[0:31:0mLogin failed. Please check your Id or password.\033[0m')
        except ValueError:
            print('\033[0:31:0mInvalid input. ID must be a number.\033[0m')
        input('Press Enter to continue...')


    # Funções de Staff (Registrar)
    def register_user_flow(self):
        self.clear_screen()
        print('=== Register New User ===')

        try:
            # Coleta de dados e valida ID
            user_id = self._safe_int_input('User ID: ')
            if user_id is None:
                raise ValueError ('User ID must be a number.')

            user_name = str(input('User name: ')).strip()
            user_email = input('User email: ').strip()
            user_cpf = input('User CPF: ').strip()
            user_password = input('User password: ').strip()

            # Criação de User
            new_user = User(user_id, user_name, user_email, user_cpf, user_password)
            
            # Registro via staff logado:
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0:31:0mNo staff logged in. Cannot register user.\033[0m')
            else:
                logged_staff.register_user(new_user)
                print('\033[0:32:0mUser registered successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    def register_staff_flow(self):
        self.clear_screen()
        print('=== Register New Staff ===')

        try:
            # Coleta de dados e valida ID
            staff_id = self._safe_int_input('Staff ID: ')
            if staff_id is None:
                raise ValueError ('Staff ID must be a number.')
            
            staff_name = input('Staff name: ').strip()
            staff_email = input('Staff email').strip()
            staff_cpf = input('Staff CPF: ').strip()
            staff_password = input('Staff password: ').strip()

            # Criação de staff
            new_staff = Staff(staff_id, staff_name, staff_email, staff_cpf, staff_password)

            # Registro via staff logado
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0:31:0mNo staff logged in. Cannot register staff.\033[0m')
            else:
                logged_staff.register_staff(new_staff)
                print('\033[0:32:0mStaff registered successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    def register_show_flow(self):
        self.clear_screen()
        print('=== Register New Show ===')

        try:
            # Coleta de dados e valida ID
            show_id = self._safe_int_input('Show ID: ')
            if show_id is None:
                raise ValueError ('Show ID must be a number.')
            
            show_date = input('Show date (YYYY-MM-DD): ').strip()
            show_name = input('Show name: ').strip()

            # Validação de data
            try:
                show_date_obj = datetime.strptime(show_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError ('Date must be in format YYYY-MM-DD.')

            # Criação de show
            new_show = Show(show_id, show_date_obj, show_name)

            # Registro via staff logado
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0:31:0mNo staff logged in. Cannot register show.\033[0m')
            else:
                logged_staff.register_show(new_show)
                print('\033[0:32:0mShow registered successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    # Funções Staff (Atualizar)
    def update_user_name(self):
        self.clear_screen()
        print('=== Update User Name ===')

        try:
            # Coleta de dados e validação de ID
            user_id = self._safe_int_input('Enter the User ID: ')
            if user_id is None:
                raise ValueError ('User ID must be a number.')
            
            new_name = input('Enter the new user name: ').strip()
            user = self.system.find_user_by_id(user_id)

            if user: 
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0:31:0mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_user_name(user, new_name)
                    print('\033[0:32:0mUser name updated successfully!\033[0m')
            else:
                print('\033[0:31:0mUser not found.\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def update_user_password(self):
        self.clear_screen()
        print('=== Update User Passoword ===')

        try:
            # Coleta de dados e validação de ID
            user_id = self._safe_int_input('Enter the User ID: ')
            if user_id is None:
                raise ValueError ('User ID must be a number.')
            
            new_password = input('Enter the new user password: ').strip()
            user = self.system.find_user_by_id(user_id)

            if user:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0:31:0mNo staff logged in. Operation not allowed.\033[0m')
                else: 
                    logged_staff.update_user_password(user, new_password)
                    print('\033[0:32:0mUser password updated successfully!\033[0m')
            else:
                print('\033[0:31:0mUser not found.\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def update_staff_name(self):
        self.clear_screen()
        print('=== Update Staff Name ===')

        try:
            # Coleta de dados e validação de ID
            staff_id = self._safe_int_input('Enter the Staff ID: ')
            if staff_id is None:
                raise ValueError ('Staff ID must be a number.')
            
            new_name = input('Enter the new staff name: ').strip()
            staff = self.system.find_staff_by_id(staff_id)

            if staff:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0:31:0mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_staff_name(staff, new_name)
                    print('\033[0:32:0mStaff name updated successfully!\033[0m')
            else:
                print('\033[0:31:0mStaff not found.\033[0m')
        
        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')

        input('Press Enter to continue....')

    def update_staff_password(self):
        self.clear_screen()
        print('=== Update Staff Password ===')

        try:
            # Coleta de dados e validação de ID
            staff_id = self._safe_int_input('Enter the Staff ID')
            if staff_id is None:
                raise ValueError ('Staff ID must be a number.')
            
            new_password = input('Enter the new staff password: ').strip()
            staff = self.system.find_staff_by_id(staff_id)

            if staff:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0:31:0mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_staff_password(staff, new_password)
                    print('\033[0:32:0mStaff password updated successfully!\033[0m')
            else:
                print('\033[0:31:0mStaff not found.\033[0m')
        
        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    # Funções Staff (Remover)
    def remove_user_flow(self):
        self.clear_screen()
        print('=== Remove User ===')

        try:
            # Coleta do ID de usuário para remoção
            user_id = self._safe_int_input('Enter the User ID to remove: ')
            if user_id is None:
                raise ValueError ('User ID must be a number.')

            # Validação se o Staff está logado
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[:31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                logged_staff.delete_user(user_id)
                print('\033[:32mUser removed successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    def remove_staff_flow(self):
        self.clear_screen()
        print('=== Remove Staff ===')

        try:
            # Coleta de dados e validação de ID
            staff_id = self._safe_int_input('Enter the Staff ID to remove: ')
            if staff_id is None:
                raise ValueError ('Staff ID must be a number.')
            
            # Validação se o staff está logado
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[:31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                logged_staff.delete_staff(staff_id)
                print('\033[:32mStaff removed successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    def remove_show_flow(self):
        self.clear_screen()
        print('=== Remove Show ===')

        try:
            # Coleta de dados e validação de ID
            show_id = self._safe_int_input('Enter the show ID to remove: ')
            if show_id is None:
                raise ValueError ('Show ID must be a number.')

            # Validação se o staff está logado
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[:31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                logged_staff.delete_show(show_id)
                print('\033[:32mShow removed successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0:31:0mError: {str(e)}\033[0m')
        
        input('Press Enter to continue...')

    # Funções Staff (Visualizar)
    def view_all_users(self):
        pass

    def view_all_staffs(self):
        pass

    def view_all_shows(self):
        pass

    # Loggout
    def logout_staff(self):
        self.system.loggout()
        print('\033[0:33:0mStaff logged out.\033[0m')
        input('Press Enter to return to login menu...')


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
            option = self._safe_int_input('Select an option: ')

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
                self.logout_staff()
            elif option == 0:
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
            option = self._safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.register_user_flow()
            elif option == 2:
                self.register_staff_flow()
            elif option == 3:
                self.register_show_flow()
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
            option = self._safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.update_user_name()
            elif option == 2:
                self.update_user_password()
            elif option == 3:
                self.update_staff_name()
            elif option == 4:
                self.update_staff_password()
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
            option = self._safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.register_user_flow()
            elif option == 2:
                self.register_staff_flow()
            elif option == 3:
                self.register_show_flow()
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
            option = self._safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 0:
                break
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')


    # Funções de User
    def view_all_shows_user(self):
        pass
    def add_show_to_favorite(self):
        pass
    def remove_show_from_favorite(self):
        pass
    def view_favorite_shows(self):
        pass
    def logout_user(self):
        print('\033[0:33:0mUser logged out.\033[0m')
        input('Press Enter to return to login menu...')

    # Menu de funcionalidade User
    def show_user_menu(self):
        while True:
            self.clear_screen()
            print(f'=== Staff Menu | Logged: {self.system.get_logged_user().name} ===')
            print('[1] View all shows')
            print('[2] Add show to favourite')
            print('[3] Remove show from favourite')
            print('[4] View favourite shows')
            print('[5] Logout')
            print('[0] Exit system')
            option = self._safe_int_input('Select an option: ')

            # Validação primária de número
            if option is None:
                print('\033[0:31:0mInvalid input. Please enter a number.\033[0m')
                input('Press Enter to continue...')
                continue

            if option == 1:
                self.view_all_shows_user()
            elif option == 2:
                self.add_show_to_favorite()
            elif option == 3:
                self.remove_show_from_favorite()
            elif option == 4:
                self.view_favorite_shows()
            elif option == 5:
                self.logout_user()
            elif option == 0:
                exit()
            else:
                print('\033[0:31:0mInvalid option. Please try again!\033[0m')
                input('Press Enter to continue...')
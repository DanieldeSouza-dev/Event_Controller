# Zona de importações

from src.core.system import SystemController
from src.core.validators import (
    safe_int_input, validate_name, validate_email, validate_password, validate_cpf
)
from src.models.staff import Staff
from src.models.user import User
from src.models.shows import Show

from datetime import datetime

class StaffFunctions:
    def __init__(self, system: SystemController):
        self.system = system

    # Funções de Staff (Registrar)
    def register_user_flow(self):
        self.system.clear_screen()
        print('=== Register New User ===')

        try:
            user_id = safe_int_input('User ID: ')
            if user_id is None:
                raise ValueError('User ID must be a number.')

            user_name = validate_name(input('User name: '))
            user_email = validate_email(input('User email: '))
            user_cpf = validate_cpf(input('User CPF: '))
            user_password = validate_password(input('User password: '))

            new_user = User(user_id, user_name, user_email, user_cpf, user_password)

            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Cannot register user.\033[0m')
            else:
                logged_staff.register_user(new_user)
                print('\033[0;32mUser registered successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def register_staff_flow(self):
        self.system.clear_screen()
        print('=== Register New Staff ===')

        try:
            staff_id = safe_int_input('Staff ID: ')
            if staff_id is None:
                raise ValueError('Staff ID must be a number.')

            staff_name = validate_name(input('Staff name: '))
            staff_email = validate_email(input('Staff email: '))
            staff_cpf = validate_cpf(input('Staff CPF: '))
            staff_password = validate_password(input('Staff password: '))

            new_staff = Staff(staff_id, staff_name, staff_email, staff_cpf, staff_password)

            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Cannot register staff.\033[0m')
            else:
                logged_staff.register_staff(new_staff)
                print('\033[0;32mStaff registered successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def register_show_flow(self):
        self.system.clear_screen()
        print('=== Register New Show ===')

        try:
            show_id = safe_int_input('Show ID: ')
            if show_id is None:
                raise ValueError('Show ID must be a number.')

            show_date = input('Show date (YYYY-MM-DD): ').strip()
            show_name = input('Show name: ').strip()

            try:
                show_date_obj = datetime.strptime(show_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Date must be in format YYYY-MM-DD.')

            new_show = Show(show_id, show_date_obj, show_name)

            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Cannot register show.\033[0m')
            else:
                logged_staff.register_show(new_show)
                print('\033[0;32mShow registered successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    # Funções Staff (Atualizar)
    def update_user_name(self):
        self.system.clear_screen()
        print('=== Update User Name ===')

        try:
            user_id = safe_int_input('Enter the User ID: ')
            if user_id is None:
                raise ValueError('User ID must be a number.')

            new_name = validate_name(input('Enter the new user name: '))
            user = self.system.find_user_by_id(user_id)

            if user:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_user_name(user, new_name)
                    print('\033[0;32mUser name updated successfully!\033[0m')
            else:
                print('\033[0;31mUser not found.\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def update_user_password(self):
        self.system.clear_screen()
        print('=== Update User Password ===')

        try:
            user_id = safe_int_input('Enter the User ID: ')
            if user_id is None:
                raise ValueError('User ID must be a number.')

            new_password = validate_password(input('Enter the new user password: '))
            user = self.system.find_user_by_id(user_id)

            if user:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_user_password(user, new_password)
                    print('\033[0;32mUser password updated successfully!\033[0m')
            else:
                print('\033[0;31mUser not found.\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def update_staff_name(self):
        self.system.clear_screen()
        print('=== Update Staff Name ===')

        try:
            staff_id = safe_int_input('Enter the Staff ID: ')
            if staff_id is None:
                raise ValueError('Staff ID must be a number.')

            new_name = validate_name(input('Enter the new staff name: '))
            staff = self.system.find_staff_by_id(staff_id)

            if staff:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_staff_name(staff, new_name)
                    print('\033[0;32mStaff name updated successfully!\033[0m')
            else:
                print('\033[0;31mStaff not found.\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def update_staff_password(self):
        self.system.clear_screen()
        print('=== Update Staff Password ===')

        try:
            staff_id = safe_int_input('Enter the Staff ID: ')
            if staff_id is None:
                raise ValueError('Staff ID must be a number.')

            new_password = validate_password(input('Enter the new staff password: '))
            staff = self.system.find_staff_by_id(staff_id)

            if staff:
                logged_staff = self.system.get_logged_staff()
                if not logged_staff:
                    print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
                else:
                    logged_staff.update_staff_password(staff, new_password)
                    print('\033[0;32mStaff password updated successfully!\033[0m')
            else:
                print('\033[0;31mStaff not found.\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    # Funções Staff (Remover)
    def remove_user_flow(self):
        self.system.clear_screen()
        print('=== Remove User ===')

        try:
            user_id = safe_int_input('Enter the User ID to remove: ')
            if user_id is None:
                raise ValueError('User ID must be a number.')

            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                logged_staff.delete_user(user_id)
                print('\033[0;32mUser removed successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def remove_staff_flow(self):
        self.system.clear_screen()
        print('=== Remove Staff ===')

        try:
            staff_id = safe_int_input('Enter the Staff ID to remove: ')
            if staff_id is None:
                raise ValueError('Staff ID must be a number.')

            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                logged_staff.delete_staff(staff_id)
                print('\033[0;32mStaff removed successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def remove_show_flow(self):
        self.system.clear_screen()
        print('=== Remove Show ===')

        try:
            show_id = safe_int_input('Enter the Show ID to remove: ')
            if show_id is None:
                raise ValueError('Show ID must be a number.')

            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                logged_staff.delete_show(show_id)
                print('\033[0;32mShow removed successfully!\033[0m')

        except ValueError as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    # Funções Staff (Visualizar)
    def view_all_users(self):
        self.system.clear_screen()
        print('=== View All Users ===')

        try:
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                users = self.system.users
                if not users:
                    print('\033[0;33mNo users registered.\033[0m')
                else:
                    logged_staff.view_user(users)

        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def view_all_staffs(self):
        self.system.clear_screen()
        print('=== View All Staffs ===')

        try:
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                staffs = self.system.staff
                logged_staff.view_staff(staffs)

        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    def view_all_shows(self):
        self.system.clear_screen()
        print('=== View All Shows ===')

        try:
            logged_staff = self.system.get_logged_staff()
            if not logged_staff:
                print('\033[0;31mNo staff logged in. Operation not allowed.\033[0m')
            else:
                shows = self.system.show
                if not shows:
                    print('\033[0;33mNo shows registered.\033[0m')
                else:
                    logged_staff.view_shows(shows)

        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    # Logout
    def logout_staff(self):
        self.system.logout()
        print('\033[0;33mStaff logged out.\033[0m')
        input('Press Enter to return to login menu...')

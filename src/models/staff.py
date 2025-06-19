#zona de importações

from __future__ import annotations
from datetime import datetime
from typing import List # Importa uma biblioteca que permite usar um List mais robusto e mais acessivel
from .person import Person
from .user import User
from .shows import Show

#criação de classe Staff
class Staff(Person):
    def __init__(self, user_id: int, name: str, password: str, email: str):
        super().__init__(user_id, name, password, email)

    #isso aqui vai servir para pegar o formato do dicionario de Person e converte para staff
    def to_dict(self) -> dict:
        staff_data = super().to_dict()
        staff_data['is_staff'] = True
        return staff_data

    @classmethod
    def from_dict(cls, data: dict) -> 'Staff':
        obj = cls.__new__(cls)
        obj._Person__id = data['id']
        obj._Person__name = data['name']
        obj._Person__email = data['email']
        obj._Person__password = data['password_hash']
        return obj


    # Funções de gerenciamento:

        # Shows:
    def register_show(self, show_data: dict) -> 'Show':
        # Valida a data digitada pelo usuario ou até mesmo pela staff
        try:
            raw_date = show_data['date']
            if isinstance(raw_date, str):
                try:
                    date = datetime.strptime(raw_date, '%Y-%m-%d')
                except ValueError:
                    raise ValueError('Date must be in format YYYY-MM-DD.')
            elif isinstance(raw_date, datetime):
                date = raw_date
            else:
                raise ValueError('Date must be a datetime object of a YYYY-MM-DD string.')

            new_show = Show(
                show_id = show_data['id'],
                name = show_data['name'],
                date = date
            )
            return new_show
        except (KeyError, ValueError) as e:
            raise ValueError(f'Invalid show data: {e}')
        
    def view_shows(self, show_list: List[Show]) -> List[dict]:
        if not isinstance(show_list, list):
            raise ValueError ('Expected a list of shows')
        displayed_shows = []
        for show in show_list:
            try:
                show_info = {
                    'ID': show.show_id,
                    'Name': show.name,
                    'Date': show.date
                }
                print(f'ID:{show.show_id} | Name:{show.name}')
                displayed_shows.append(show_info)
            except AttributeError as e:
                print(f'Skipped invalid show entry: {e}')
        return displayed_shows
    

        # Usuários:    
    def register_user(self, user_data: dict) -> 'User':
        try:
            password = user_data['password']
            new_user = User(
                user_id = user_data['id'],
                name = user_data['name'],
                email = user_data['email'],
                password = password
            )
            return new_user
        except (KeyError, ValueError) as e:
            raise ValueError(f'Invalid user data: {e}')

    # Função para ver o usuários cadastrados
    def view_user(self, users: List) -> List:
        if not isinstance(users, list):
            raise ValueError ('Expected a list of users')

        displayed_users = []
        for user in users:
            try:
                user_info = {
                  'ID': user.id,
                  'Name': user.name,
                  'Email': user.email
                }
                print(f'ID:{user.id} | Name:{user.name}')
                displayed_users.append(user_info)
            except AttributeError as e:
                print(f'Skipped invalid user entry: {e}')

        return displayed_users

    def update_user_name(self, user: User, new_name: str) -> None:
        user.update_name(new_name)

    def update_user_password(self, user: User, new_password: str) -> None:
        user.update_password(new_password)


        # Staff:
    def register_staff (self, staff_data: dict) -> 'Staff':
        try:
            password = staff_data['password']
            new_staff = Staff(
                user_id=staff_data['id'],
                name=staff_data['name'],
                email=staff_data['email'],
                password=password
            )
            return new_staff
        except (KeyError, ValueError) as e:
            raise ValueError(f'Invalid staff data: {e}')

    def view_staff(self, staff_list: List['Staff']) -> List[dict]:
        if not isinstance(staff_list, list):
            raise ValueError ('Expected a list of staff')

        displayed_staff = []
        for staff_member in staff_list:
            try:
                staff_info = {
                    'ID': staff_member.id,
                    'Name': staff_member.name,
                    'Email': staff_member.email
                }
                print(f'ID:{staff_member.id} | Name:{staff_member.name}')
                displayed_staff.append(staff_info)
            except AttributeError as e:
                print(f'Skipped invalid staff entry: {e}')

        return displayed_staff

    def update_staff_name(self, staff: 'Staff', new_name: str) -> None:
        staff.update_name(new_name)

    def update_staff_password(self, staff: 'Staff', new_password: str) -> None:
        staff.update_password(new_password)

    # Zona criada para deletar usuário, staff e shows caso necessário

    def delete_user(self, users_list: List[User], user_id: int) -> bool:
        for i, user in enumerate(users_list):
            if user.id == user_id:
                del users_list[i]
                print(f'Deleted user {user.id} from list {i}')
                return True
        print(f'User {user_id} not found.')
        return False

    def delete_staff(self, staff_list: List[Staff], staff_id: int) -> bool:
        for i, staff in enumerate(staff_list):
            if staff.id == staff_id:
                del staff_list[i]
                print(f'Deleted staff {staff.id} from list {i}')
                return True
        print(f'Staff {staff_id} not found.')
        return False

    def delete_show(self, show_list: List[Show], show_id: int) -> bool:
        for i, show in enumerate(show_list):
            if show.show_id == show_id:
                del show_list[i]
                print(f'Deleted show {show.id} from list {i}')
                return True
        print(f'Show {show_id} not found.')
        return False
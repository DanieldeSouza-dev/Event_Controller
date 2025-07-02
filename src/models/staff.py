# Zona de importações

from __future__ import annotations
from datetime import datetime
from typing import List
from .person import Person
from .user import User
from .shows import Show

# Criação da classe Staff
class Staff(Person):
    def __init__(self, user_id: int, name: str, email: str, cpf: str, password: str):
        super().__init__(user_id, name, email, cpf, password)
        # Removido o atributo system para evitar dependência circular

    # Método para converter Staff em dict (útil para salvar em JSON)
    def to_dict(self) -> dict:
        staff_data = super().to_dict()
        staff_data['is_staff'] = True
        staff_data['masked_cpf'] = self.masked_cpf
        return staff_data

    # Cria um objeto Staff a partir de um dicionário (ex: JSON)
    @classmethod
    def from_dict(cls, data: dict) -> Staff:
        obj = cls.__new__(cls)
        obj._Person__id = data['id']
        obj._Person__name = data['name']
        obj._Person__email = data['email']
        obj._Person__cpf = data['cpf']
        obj._Person__password = data['password_hash']
        return obj

    # Registro de Shows
    def register_show(self, new_show: Show, show_list: List[Show]) -> None:
        show_list.append(new_show)

    # Visualização de Shows
    def view_shows(self, show_list: List[Show]) -> None:
        if not isinstance(show_list, list):
            raise ValueError('Expected a list of shows')
        if not show_list:
            print('\033[0;33mNo shows registered.\033[0m')
            return
        for show in show_list:
            print(f'ID:{show.show_id} | Name:{show.name} | Date:{show.date.strftime("%Y-%m-%d")}')

    # Registro de Usuários
    def register_user(self, user: User, users_list: List[User]) -> None:
        users_list.append(user)

    # Visualização de Usuários
    def view_user(self, users_list: List[User]) -> None:
        if not isinstance(users_list, list):
            raise ValueError('Expected a list of users')
        if not users_list:
            print('\033[0;33mNo users registered.\033[0m')
            return
        for user in users_list:
            print(f'ID:{user.id} | Name:{user.name} | Email:{user.email} | CPF:{user.masked_cpf}')

    # Atualizar nome do usuário
    def update_user_name(self, user: User, new_name: str) -> None:
        user.update_name(new_name)

    # Atualizar senha do usuário
    def update_user_password(self, user: User, new_password: str) -> None:
        user.update_password(new_password)

    # Registro de Staff (passar objeto Staff e lista para adicionar)
    def register_staff(self, new_staff: Staff, staff_list: List[Staff]) -> None:
        staff_list.append(new_staff)

    # Visualização de Staff
    def view_staff(self, staff_list: List[Staff]) -> None:
        if not isinstance(staff_list, list):
            raise ValueError('Expected a list of staff')
        if not staff_list:
            print('\033[0;33mNo staff registered.\033[0m')
            return
        for staff_member in staff_list:
            print(f'ID:{staff_member.id} | Name:{staff_member.name} | Email:{staff_member.email} | CPF:{staff_member.masked_cpf}')

    # Atualizar nome do staff
    def update_staff_name(self, staff: Staff, new_name: str) -> None:
        staff.update_name(new_name)

    # Atualizar senha do staff
    def update_staff_password(self, staff: Staff, new_password: str) -> None:
        staff.update_password(new_password)

    # Deletar usuário pelo ID
    def delete_user(self, users_list: List[User], user_id: int) -> bool:
        for i, user in enumerate(users_list):
            if user.id == user_id:
                del users_list[i]
                print(f'User with ID {user_id} deleted successfully.')
                return True
        print(f'User with ID {user_id} not found.')
        return False

    # Deletar staff pelo ID
    def delete_staff(self, staff_list: List[Staff], staff_id: int) -> bool:
        for i, staff in enumerate(staff_list):
            if staff.id == staff_id:
                del staff_list[i]
                print(f'Staff with ID {staff_id} deleted successfully.')
                return True
        print(f'Staff with ID {staff_id} not found.')
        return False

    # Deletar show pelo ID
    def delete_show(self, show_list: List[Show], show_id: int) -> bool:
        for i, show in enumerate(show_list):
            if show.show_id == show_id:
                del show_list[i]
                print(f'Show with ID {show_id} deleted successfully.')
                return True
        print(f'Show with ID {show_id} not found.')
        return False

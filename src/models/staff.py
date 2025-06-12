#zona de importações

from datetime import datetime
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

    # Função para ver o usuários cadastrados
    def view_user(self, users: list) -> list:
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
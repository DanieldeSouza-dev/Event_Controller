from .person import Person
from typing import List
from src.models.shows import Show

class User(Person):
    def __init__(self, user_id: int, name: str, email: str, cpf: str, password: str):
        super().__init__(user_id, name, email, cpf, password)
        self.__favorites = []

    def to_dict(self) -> dict:
        user_data = super().to_dict()
        user_data['favorites'] = self.__favorites
        user_data['masked_cpf'] = self.masked_cpf
        return user_data

    def view_shows(self, show_list: List[Show]) -> List[dict]:
        if not isinstance(show_list, list):
            raise ValueError('Expected a list of shows')

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

    def add_favorites(self, event_id: int) -> None:
        if event_id not in self.__favorites:
            self.__favorites.append(event_id)
            print(f'{event_id} added to favorites list')
        else:
            print(f'{event_id} is already in favorites list')

    def remove_favorites(self, event_id: int) -> bool:
        if event_id in self.__favorites:
            self.__favorites.remove(event_id)
            print(f'{event_id} removed successfully')
            return True
        else:
            print(f'{event_id} is not in favorites list')
            return False

    def get_favorite_shows(self, all_shows: List[Show]) -> List[Show]:
        return [show for show in all_shows if show.show_id in self.__favorites]

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        obj = cls.__new__(cls)
        obj._Person__id = data['id']
        obj._Person__name = data['name']
        obj._Person__email = data['email']
        obj._Person__password = data['password_hash']
        obj._Person__cpf = data['cpf']
        obj._User__favorites = data.get('favorites', [])
        return obj

    @property
    def favorites(self):
        return self.__favorites

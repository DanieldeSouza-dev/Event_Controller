from .person import Person

class User(Person):
    def __init__(self, user_id: int, name: str, password: str):
        super().__init__(user_id, name, password)
        self.__favorites = []

    def to_dict(self) -> dict:
        user_data = super().to_dict()
        user_data['favorites'] = self.__favorites
        return user_data

    def add_favorites(self, event_id: int) -> None:
        self.__favorites.append(event_id)

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        obj = cls.__new__(cls)
        obj.__Person__id = data['id']
        obj.__Person__name = data['name']
        obj.__Person__password = data['password_hash']
        obj.__favorites = data.get('favorites', [])
        return obj

    # Adicionei o @property para poder resgatar os dados facilmente para testes
    @property
    def favorites(self):
        return self.__favorites
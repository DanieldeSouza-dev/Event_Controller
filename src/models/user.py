from person import Person

class User(Person):
    def __init__(self, user_id: int, name: str, password: str):
        super().__init__(user_id, name, password)
        self.__favourites = []

    def to_dict(self) -> dict:
        user_data = super().to_dict()
        user_data['favourites'] = self.__favourites
        return user_data

    def add_favourites(self, event_id: int) -> None:
        self.__favourites.append(event_id)

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        obj = cls.__new__(cls)
        obj.__Person__id = data['id']
        obj.__Person__name = data['name']
        obj.__Person__password = data['password_hash']
        obj.__favourites = data.get('favourites', [])
        return obj
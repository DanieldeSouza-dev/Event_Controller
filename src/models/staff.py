from person import Person

class Staff(Person):
    def __init__(self, user_id: int, name: str, password: str):
        super().__init__(user_id, name, password)

    def to_dict(self) -> dict:
        staff_data = super().to_dict()
        staff_data['is_staff'] = True
        return staff_data

    @classmethod
    def from_dict(cls, data: dict) -> 'Staff':
        obj = cls.__new__(cls)
        obj.__Person__id = data['id']
        obj.__Person__name = data['name']
        obj.__Person__password = data['password_hash']
        obj.__favourites = data.get('favourites', [])
        return obj

    # def register_user(self, user_data: dict) -> 'User': #Falta implementar as demais funções

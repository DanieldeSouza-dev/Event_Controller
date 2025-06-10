from passlib.hash import pbkdf2_sha256 # biblioteca que irá armazenar a senha de maneira mais segura

class Person:
    def __init__(self, user_id, name, password):
        self.__id = self.validate_id(user_id)
        self.__name = self.validate_name(name)
        valid_password = self.validate_password(password)
        self.__password = self._hash_password(password) #armazena o hash da senha

    def validate_id(self, user_id: int) -> int:
        if not isinstance(user_id, int) or user_id <=0:
            raise ValueError("Invalid user_id")
        return user_id

    def validate_name(self, name: str) -> str:
        if not name or not isinstance(name, str):
            raise ValueError("Invalid name")
        return name.strip()

    def validate_password(self, password: str) -> str:
        if not isinstance(password, str) or len(password) < 6:
            raise ValueError("Passwords must be at least 6 characters.")
        return password

    def _hash_password(self, password: str) -> str:
        return pbkdf2_sha256.hash(password) # aqui a biblioteca vai gerar a senha em hash

    def verify_password(self, input_password: str) -> bool:
        return pbkdf2_sha256.verify(input_password, self.__password)

    def to_dict(self) -> dict: #prepara a classe para ser salva em JSON (transforma em dicionario os resultados da classe)
        return {
            'id': self.__id,
            'name': self.__name,
            'password_hash': self.__password,
            'is_staff': False
        }

    def update_name(self, new_name: str) -> None: #será usado para renomear usuarios/staff já cadastrados
        self.__name = self.validate_name(new_name)

    def update_password(self, new_password: str) -> None: #será usado para alterar senha de usuario/staff ja cadastrado
        valid_password = self.validate_password(new_password)
        self.__password = self._hash_password(new_password)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self):
        return f'Person(id={self.__id}, name={self.__name})'

    def __repr__(self):
        return f'Person(id={self.__id}, name={self.__name})'
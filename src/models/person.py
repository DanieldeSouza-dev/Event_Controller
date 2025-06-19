# Zona de importações

from passlib.hash import pbkdf2_sha256
from src.core.validators import validate_id, validate_name, validate_email, validate_password, validate_cpf

class Person:
    def __init__(self, user_id, name, password, email, cpf):
        self.__id = validate_id(user_id)
        self.__name = validate_name(name)
        self.__email = validate_email(email)
        validate_password(password)
        self.__password = self._hash_password(password) #armazena o hash da senha
        self.__cpf = validate_cpf(cpf)

    # Criação de senha em hash
    def _hash_password(self, password: str) -> str:
        return pbkdf2_sha256.hash(password) # aqui a biblioteca vai gerar a senha em hash

    # Verifica se a senha está sendo hasheada
    def verify_password(self, input_password: str) -> bool:
        return pbkdf2_sha256.verify(input_password, self.__password)

    # Máscara de cpf para maior segurança
    @property # Tive que colocar o property aqui direto na função para poder pegar ela mais facilmente
    def masked_cpf(self) -> str:
        return f'***.{self.__cpf[3:6]}.{self.__cpf[6:9]}-**'


    # Prepara a classe para ser salva em JSON (transforma em dicionario os resultados da classe)
    def to_dict(self) -> dict:
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'password_hash': self.__password,
            'cpf': self.__cpf,
            'is_staff': False
        }

    # Zona para fazer alterações de nome e senha futuramente pelo staff
    def update_name(self, new_name: str) -> None:
        self.__name = validate_name(new_name)

    def update_password(self, new_password: str) -> None:
        validate_password(new_password)
        self.__password = self._hash_password(new_password)


    # Sessão "@property" usada para acesso de leitura e não de escrita, evita alterações no código fonte.
    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email
    
    @property # Esse SÓ poderá ser usado no backend e funções internas
    def cpf(self) -> str:
        return self.__cpf

    # Útil para a visualização do usuario no print(objeto). Mais legível
    def __str__(self):
        return f'Person(id={self.__id}, name={self.__name}, cpf={self.masked_cpf()})'

    # Útil para dev em debug. Mais preciso
    def __repr__(self):
        return f'Person(id={self.__id}, name={self.__name}, cpf={self.masked_cpf()})'
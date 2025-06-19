import re

# Parte das validações:
def validate_id(user_id: int) -> int:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("Invalid user_id")
    return user_id


def validate_name(name: str) -> str:
    if not name or not isinstance(name, str):
        raise ValueError("Invalid name")
    return name.strip()


def validate_email(email: str) -> str:
    if not email or not isinstance(email, str):
        raise ValueError("Invalid email")
    return email.strip()


def validate_password(password: str) -> str:
    if not isinstance(password, str) or len(password) < 6:
        raise ValueError("Passwords must be at least 6 characters.")
    return password

# Limpa o cpf que foi cadastrado para apenas numeros e retorna
def sanitize_cpf(raw_cpf: str) -> str:
    if not isinstance(raw_cpf, str):
        raise ValueError('CPF must be a string')
    cleaned_cpf = re.sub(r'[\.\-\s]', '', raw_cpf)
    return cleaned_cpf

def validate_cpf(cpf: str) -> str:
    cpf = sanitize_cpf(cpf)

    if not cpf.isdigit():
        raise ValueError("Invalid cpf: must contain only digits")
    if len(cpf) != 11:
        raise ValueError("Invalid cpf: must have 11 digits")
    if cpf == cpf[0] * 11:
        raise ValueError("Invalid cpf: repeated digits")

    # Valida o primeiro digito do verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digit1 = 0
    else:
        digit1 = 11 - resto
    if digit1 != int(cpf[9]):
        raise ValueError("Invalid cpf: first check digit does not match")

    # Valida o segundo digito do verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digit2 = 0
    else:
        digit2 = 11 - resto
    if digit2 != int(cpf[10]):
        raise ValueError("Invalid cpf: second check digit does not match")

    return cpf
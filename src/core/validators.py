import re

# Parte das validações:
def validate_id(user_id: int) -> int:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("Invalid user_id")
    return user_id


def validate_name(name: str) -> str:
    if not name or not isinstance(name, str):
        raise ValueError("Invalid name")
    
    name = name.strip()
    if len(name) < 2:
        raise ValueError ('Name too short.')
    
    return name

def validate_email(email: str) -> str:
    if not email or not isinstance(email, str):
        raise ValueError("Invalid email")
    
    email = email.strip()
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError ('Email must contain "@" and a valid domain.')
    
    return email


def validate_password(password: str) -> str:
    if not isinstance(password, str) or len(password) < 6:
        raise ValueError("Passwords must be at least 6 characters.")
    return password

# Valida se o número digitado era um número inteiro mesmo ou se era outra coisa
def safe_int_input(prompt: str) -> int | None:
    try:
        return int(input(prompt))
    except ValueError:
        return None

# Limpa o cpf que foi cadastrado para apenas numeros e retorna
def sanitize_cpf(raw_cpf: str) -> str:
    if not isinstance(raw_cpf, str):
        raise ValueError('CPF must be a string')
    cleaned_cpf = re.sub(r'[\.\-\s]', '', raw_cpf)
    return cleaned_cpf

def validate_cpf(cpf: str) -> str:
    cpf = sanitize_cpf(cpf)

    if not cpf.isdigit():
        raise ValueError("Invalid CPF: must contain only digits")
    if len(cpf) != 11:
        raise ValueError("Invalid CPF: must have 11 digits")
    if cpf == cpf[0] * 11:
        raise ValueError("Invalid CPF: repeated digits")

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
        raise ValueError("Invalid CPF: first check digit does not match")

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
        raise ValueError("Invalid CPF: second check digit does not match")

    return cpf
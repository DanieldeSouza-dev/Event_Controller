# Zona de importação

import os
import json
from typing import List
from src.models.user import User
from src.models.staff import Staff
from src.models.shows import Show

# Procura os aqruivos para inicio de persistência
DATA_DIR = os.path.join('src', 'data')
FAV_DIR = os.path.join(DATA_DIR, 'favorites')

def ensure_data_directories():
    os.makedirs(DATA_DIR, existe_ok=True)
    os.makedirs(FAV_DIR, exist_ok=True)

def save_users(users = List[User]):
    pass

def load_users() -> List[User]:
    pass

def save_staff(staff_list: List[Staff]):
    data = [staff.to_dict() for staff in staff_list]
    with open(os.path.join(DATA_DIR, 'staff.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_staff() -> List[Staff]:
    pass

def save_shows(shows: List[Show]):
    pass

def load_shows() -> List[Show]:
    pass

def save_user_favorites(user: User):
    pass

def load_user_favorites(user: User):
    pass

# Cria um Staff padrão para que o usuário consiga usar as funcionalidades
def create_default_staff_if_needed():
    path = os.path.join(DATA_DIR, 'staff.json')
    if not os.path.exists(path):
        staff = Staff(
            user_id = 1,
            name = 'Admin',
            email = 'admin@gmail.com',
            cpf = '79404528005',
            password = 'admin1234'
        )
        save_staff([Staff])

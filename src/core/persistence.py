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
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(FAV_DIR, exist_ok=True)

def save_users(users: List[User]):
    data = [user.to_dict() for user in users]
    with open(os.path.join(DATA_DIR, 'users.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_users() -> List[User]:
    path = os.path.join(DATA_DIR, 'users.json')
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [User.from_dict(d) for d in data]

def save_staff(staff_list: List[Staff]):
    data = [staff.to_dict() for staff in staff_list]
    with open(os.path.join(DATA_DIR, 'staff.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_staff() -> List[Staff]:
    path = os.path.join(DATA_DIR, 'staff.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Staff.from_dict(d) for d in data] 

def save_shows(shows: List[Show]):
    data = [show.to_dict() for show in shows]
    with open(os.path.join(DATA_DIR, 'shows.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_shows() -> List[Show]:
    path = os.path.join(DATA_DIR, 'shows.json')
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Show.from_dict(d) for d in data]

def save_user_favorites(user: User):
    path = os.path.join(FAV_DIR, f'user_{user.id}_favorites.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(user.favorites, f, indent=4)

def load_user_favorites(user: User):
    path = os.path.join(FAV_DIR, f'user_{user.id}_favorites.json')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as f:
            user._User__favorites = json.load(f)

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
        save_staff([staff])

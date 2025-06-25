# Zona de importação

from src.models.user import User
from src.models.staff import Staff

def authenticate_user(user_id: int, password: str, user_list: list[User]) -> User | None:
    for user in user_list:
        if user.id == user_id and user.verify_password(password):
            return user
    return None

def authenticate_staff(staff_id: int, password: str, staff_list: list[Staff]) -> Staff | None:
    for staff in staff_list:
        if staff.id == staff_id and staff.verify_password(password):
            return staff
    return None
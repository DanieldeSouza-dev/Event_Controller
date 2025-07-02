import os
from src.core.authentication import authenticate_staff, authenticate_user
from src.models.staff import Staff
from src.models.user import User
from src.models.shows import Show

class SystemController:
    def __init__(self, users: list[User], staff: list[Staff], shows: list[Show]):
        self.users = users
        self.staff = staff
        self.shows = shows  # plural agora
        self.current_user = None
        self.current_staff = None

    def login_user(self, user_id: int, password: str) -> bool:
        user = authenticate_user(user_id, password, self.users)
        if user:
            self.current_user = user
            return True
        return False

    def login_staff(self, staff_id: int, password: str) -> bool:
        staff = authenticate_staff(staff_id, password, self.staff)
        if staff:
            self.current_staff = staff
            return True
        return False

    def find_user_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def find_staff_by_id(self, staff_id: int) -> Staff | None:
        for staff in self.staff:
            if staff.id == staff_id:
                return staff
        return None

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def logout_user(self):
        self.current_user = None

    def logout_staff(self):
        self.current_staff = None

    def logout(self):
        self.logout_user()
        self.logout_staff()

    def get_logged_user(self):
        return self.current_user

    def get_logged_staff(self):
        return self.current_staff

    def is_user_logged(self) -> bool:
        return self.current_user is not None

    def is_staff_logged(self) -> bool:
        return self.current_staff is not None

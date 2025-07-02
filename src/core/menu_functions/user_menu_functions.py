# Zona de importações

from src.core.system import SystemController
from src.core.validators import safe_int_input
from src.core.persistence import save_user_favorites  # Adicionado para salvar favoritos

class UserFunctions:
    def __init__(self, system: SystemController):
        self.system = system

    # Visualizar todos os Shows
    def view_all_shows_user(self):
        self.system.clear_screen()
        print('=== View All Shows ===')

        try:
            logged_user = self.system.get_logged_user()
            if not logged_user:
                print('\033[0;31mNo user logged in. Operation not allowed.\033[0m')
            else:
                shows = self.system.shows
                if not shows:
                    print('\033[0;33mNo shows available.\033[0m')
                else:
                    logged_user.view_shows(shows)
        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    # Adicionar show ao favorito
    def add_show_to_favorite(self):
        self.system.clear_screen()
        print('=== Add Show To Favorites ===')

        try:
            logged_user = self.system.get_logged_user()
            if not logged_user:
                print('\033[0;31mNo user logged in. Operation not allowed.\033[0m')
                return

            show_id = safe_int_input('Enter the Show ID: ')
            if show_id is None:
                raise ValueError('Show ID must be a number.')

            show_exists = any(show.show_id == show_id for show in self.system.shows)
            if not show_exists:
                print('\033[0;31mShow not found.\033[0m')
            else:
                logged_user.add_favorites(show_id)
                save_user_favorites(logged_user)  # Salva após adicionar
                print('\033[0;32mShow added to favorites.\033[0m')

        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

        input('Press Enter to continue...')

    # Remover show dos favoritos
    def remove_show_from_favorite(self):
        self.system.clear_screen()
        print('=== Remove Show From Favorites ===')

        try:
            logged_user = self.system.get_logged_user()
            if not logged_user:
                print('\033[0;31mNo user logged in. Operation not allowed.\033[0m')
                return

            show_id = safe_int_input('Enter the Show ID: ')
            if show_id is None:
                raise ValueError('Show ID must be a number.')

            removed = logged_user.remove_favorites(show_id)
            if removed:
                save_user_favorites(logged_user)  # Salva após remover
                print('\033[0;32mShow removed from favorites.\033[0m')
            else:
                print('\033[0;33mShow not found in favorites.\033[0m')

        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

    # Visualizar apenas os shows favoritos
    def view_favorite_shows(self):
        self.system.clear_screen()
        print('=== View All Favorites ===')

        try:
            logged_user = self.system.get_logged_user()
            if not logged_user:
                print('\033[0;31mNo user logged in. Operation not allowed.\033[0m')
            else:
                favorites = logged_user.get_favorite_shows(self.system.shows)
                if not favorites:
                    print('\033[0;33mYou have no favorite shows.\033[0m')
                else:
                    for show in favorites:
                        print(f'ID: {show.show_id} | Name: {show.name} | Date: {show.date.strftime("%Y-%m-%d")}')
        except Exception as e:
            print(f'\033[0;31mError: {str(e)}\033[0m')

    def logout_user(self):
        self.system.logout()
        print('\033[0;33mUser logged out.\033[0m')
        input('Press Enter to return to login menu...')

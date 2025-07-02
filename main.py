# Zona de importação

from src.interface.menu import Interface
from src.core.system import SystemController
from src.core.persistence import (
    ensure_data_directories, load_staff, load_users, load_shows,
    create_default_staff_if_needed, load_user_favorites
)

# Main
def main():
    # Garante que as pastas de dados existem
    ensure_data_directories()

    # Cria o Staff padrão se não existir
    create_default_staff_if_needed()

    # Carrega os dados que existem
    staff_list = load_staff()
    user_list = load_users()
    show_list = load_shows()

    # Carrega favoritos individuais de cada usuário
    for user in user_list:
        load_user_favorites(user)

    # Cria o controlador do sistema com os dados carregados
    system = SystemController(users=user_list, staff=staff_list, shows=show_list)

    # Cria a interface (menu) passando o controlador
    interface = Interface(system)

    # Inicia o menu principal (ou login)
    interface.run()

if __name__ == '__main__':
    main()

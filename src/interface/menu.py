class Interface:
    def __init__(self, sistema):
        self.sistema = sistema

    def exibir_menu(self):
        while True:
            print('====Menu====')
            print('Ver shows [1]')
            print('Cadastrar shows [2]')
            print('Cadastrar usuário [3]')
            print('Ver show favorito do usuário [4]')
            print('Adicionar show favorito no usuário [5]')
            print('Sair [0]')
            opcao = input('\nEscolha uma opção: ')

            if opcao == '1':
                self.sistema.listar_shows()
            elif opcao == '2':
                nome = input('Nome do show: ')
                cidade = input('Cidade: ')
                self.sistema.adicionar_show(nome, cidade)
            elif opcao == '3':
                nome_usuario = input('Nome do usuário: ')
                self.sistema.cadastrar_usuario(nome_usuario)
            elif opcao == '4':
                nome_usuario = input('Digite o nome do usuário:')
                self.sistema.ver_favoritos_usuario(nome_usuario)
            elif opcao == '5':
                nome_usuario = input('Nome do usuário: ')
                self.sistema.adicionar_show_favorito_usuario(nome_usuario)
            elif opcao == '0':
                print('Saindo...')
                break
            else:
                print('Opção inválida, tente novamente!')
import os

restaurantes = [{'Nome':'Sushi', 'Categoria':'Japonesa', 'ativo':False}, 
                {'Nome':'Pizza', 'Categoria':'Italiana', 'ativo':True}, 
                {'Nome':'Taco', 'Categoria':'Mexicana', 'ativo':False}
]

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_nome_app():
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    ''')

def exibir_opcoes():
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Ativar/desativar restaurante')
    print ('4. Sair do app \n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()

def voltar_menu_principal():
    input('Digite um tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos Restaurantes\n')

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}:')
    dados_do_restaurante = {'Nome':nome_restaurante, 'Categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes\n')

    print(f'{'Nome Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alternar_status_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante:')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        alternar_status_restaurante()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            alternar_status_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



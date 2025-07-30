import os

restaurants = [ {'name':'Na Brasa Cozinha', 'category':'Brasileira', 'active':False},
                {'name':'Pizza Suprema', 'category':'Pizza', 'active':True},
                {'name':'Grão & Grelha', 'category':'Hamburguer', 'active':False}]

def display_name():
    '''Exibe o nome do aplicativo na tela inicial'''
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝓼𝓹𝓻𝓮𝓼𝓼\n')

def display_options():
    '''Exibe as opções disponíveis no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Atividade do restaurante')
    print('4. Sair\n')

def register_new_restaurant():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    display_subtitle('Cadastro de novos restaurantes')

    name = input('Digite o nome do restaurante que deseja cadastrar: ')
    category = input(f'Digite a categoria do restaurante {name}: ')
    restaurant_data = {'name':name, 'category':category, 'active':False}
    restaurants.append(restaurant_data)
    print(f'O restaurante {name} foi cadastrado com sucesso')
    back_to_main_menu()

def list_restaurants():
    '''Lista todos os restaurantes cadastrados, mostrando nome, categoria e status

    Output:
    - Exibe a lista de restaurantes formatada
    '''
    display_subtitle('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_activity = 'Ativado' if restaurant['active'] else 'Desativado'
        print(f'- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_activity}')
    back_to_main_menu()

def toggle_restaurant_state():
    '''Alterna o estado (ativo/desativado) de um restaurante pelo nome informado

    Inputs:
    - Nome do restaurante

    Output:
    - Atualiza o status do restaurante ou informa se não encontrado
    '''
    display_subtitle('Alterando estado do restaurante')
    
    restaurant_name = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurant_found = False
    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'O restaurante {restaurant_name} foi ativado com sucesso' if restaurant['active'] else f'O restaurante {restaurant_name} foi desativado com sucesso'
            print(message)

    if not restaurant_found:
        print('O restaurante não foi encontrado')

    back_to_main_menu()

def end_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    display_subtitle('Encerrando app...')

def invalid_option():
    '''Exibe mensagem de opção inválida e retorna ao menu principal

    Output:
    - Mensagem de erro e redirecionamento ao menu
    '''
    display_subtitle('Opção inválida!')
    back_to_main_menu()

def back_to_main_menu():
    '''Solicita confirmação do usuário e retorna ao menu principal

    Output:
    - Aguarda entrada do usuário para exibir o menu principal novamente
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def display_subtitle(text):
    ''' Exibe um subtítulo estilizado na tela 

    Inputs:
    - text: str - O texto do subtítulo

    Output:
    - Exibe subtítulo com formatação visual
    '''
    os.system('cls')
    line = '-' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def choose_option():
    '''Solicita uma opção do usuário, chama a função correspondente e trata entradas inválidas

    Inputs:
    - Opção numérica do menu principal

    Output:
    - Executa a ação relacionada à opção escolhida ou exibe erro em caso de entrada inválida
    '''
    try:
        option_chosen = int(input('Escolha uma opção: '))
        match option_chosen:
            case 1:
                register_new_restaurant()
            case 2:
                list_restaurants()
            case 3:
                toggle_restaurant_state()
            case 4:
                end_app()
            case _:
                invalid_option()
    except:
        invalid_option()
        
def main():
    '''Função principal que inicializa o app e exibe o menu'''
    os.system('cls')
    display_name()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
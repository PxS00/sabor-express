import os

restaurants = [ {'name':'Na Brasa Cozinha', 'category':'Brasileira', 'active':False},
                {'name':'Pizza Suprema', 'category':'Pizza', 'active':True},
                {'name':'Grão & Grelha', 'category':'Hamburguer', 'active':False}]

def display_name():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝓼𝓹𝓻𝓮𝓼𝓼\n')

def display_options():
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
    display_subtitle('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_activity = 'Ativado' if restaurant['active'] else 'Desativado'
        print(f'- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_activity}')
    back_to_main_menu()

def toggle_restaurant_state():
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
    display_subtitle('Encerrando app...')

def invalid_option():
    display_subtitle('Opção inválida!')
    back_to_main_menu()

def back_to_main_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def display_subtitle(text):
    os.system('cls')
    line = '-' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def choose_option():
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
    os.system('cls')
    display_name()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
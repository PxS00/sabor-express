import os

restaurants = ['Na Brasa Cozinha', 'Flor do Manjericão']

def display_name():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝓼𝓹𝓻𝓮𝓼𝓼\n')

def display_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def register_new_restaurant():
    display_subtitle('Cadastro de novos restaurantes')
    print('\n')
    restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurants.append(restaurant_name)
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso')
    back_to_main_menu()

def list_restaurants():
    display_subtitle('Listando restaurantes')
    print('\n')
    for restaurant in restaurants:
        print(f'. {restaurant}')
    back_to_main_menu()

def invalid_option():
    print('Opção inválida!\n')
    back_to_main_menu()

def end_app():
    display_subtitle('Encerrando app...')
    print('\n')

def back_to_main_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def display_subtitle(text):
    os.system('cls')
    print(text)

def choose_option():
    try:
        option_chosen = int(input('Escolha uma opção: '))
        match option_chosen:
            case 1:
                register_new_restaurant()
            case 2:
                list_restaurants()
            case 3:
                print('Ativar restaurante')
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
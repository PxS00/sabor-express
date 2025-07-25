import os

restaurants = []

def display_name():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝓼𝓹𝓻𝓮𝓼𝓼\n')

def display_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def register_new_restaurant():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurants.append(restaurant_name)
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def end_app():
    os.system('cls')
    print('Encerrando app...\n')

def invalid_option():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def choose_option():
    try:
        option_chosen = int(input('Escolha uma opção: '))
        match option_chosen:
            case 1:
                register_new_restaurant()
            case 2:
                print('Listar restaurantes')
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
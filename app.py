from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish

restaurant_pizza_suprema = Restaurant('Pizza Suprema', 'Pizzaria')
restaurant_pizza_suprema.toggle_state()


restaurant_grao_e_grelha = Restaurant('Grão & Grelha', 'Hamburguer')
restaurant_na_brasa_cozinha = Restaurant('Na Brasa Cozinha', 'Brasileira')

drink_watermelon_juice = Drink('Suco de Melancia', 5.0, 'Grande')
dish_paozinho = Dish('Paozinho', 2.00, 'O melhor pão da cidade')
restaurant_na_brasa_cozinha.add_to_menu(drink_watermelon_juice)
restaurant_na_brasa_cozinha.add_to_menu(dish_paozinho)

def main():
    restaurant_na_brasa_cozinha.show_menu
    

if __name__ == '__main__':
    main()
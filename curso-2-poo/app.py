from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish
from models.menu.dessert import Dessert

restaurant_pizza_suprema = Restaurant('Pizza Suprema', 'Pizzaria')
restaurant_pizza_suprema.toggle_state()

restaurant_grao_e_grelha = Restaurant('Grão & Grelha', 'Hamburguer')
restaurant_na_brasa_cozinha = Restaurant('Na Brasa Cozinha', 'Brasileira')

drink_watermelon_juice = Drink('Suco de Melancia', 5.0, 'Grande')
drink_watermelon_juice.apply_discount()
dish_paozinho = Dish('Paozinho', 2.00, 'O melhor pão da cidade')
dish_paozinho.apply_discount()
dessert_mousse_maracuja = Dessert('Mousse de Maracujá', 7.00,'Sobremesa Gelada', 'Individual', 'Leve e refrescante')
restaurant_na_brasa_cozinha.add_to_menu(dessert_mousse_maracuja)
restaurant_na_brasa_cozinha.add_to_menu(drink_watermelon_juice)
restaurant_na_brasa_cozinha.add_to_menu(dish_paozinho)

def main():
    restaurant_na_brasa_cozinha.show_menu
    

if __name__ == '__main__':
    main()
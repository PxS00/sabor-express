from models.restaurant import Restaurant

restaurant_pizza_suprema = Restaurant('Pizza Suprema', 'Pizzaria')
restaurant_pizza_suprema.toggle_state()
restaurant_pizza_suprema.receive_rating('Anna', 10)
restaurant_pizza_suprema.receive_rating('Kel', 6)

restaurant_grao_e_grelha = Restaurant('Grão & Grelha', 'Hamburguer')
restaurant_na_brasa_cozinha = Restaurant('Na Brasa Cozinha', 'Brasileira')

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()
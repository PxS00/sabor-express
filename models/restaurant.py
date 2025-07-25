class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def __str__(self) -> str:
        return f'{self.name} | {self.category}'
    
    def list_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name} | {restaurant.category} | {restaurant.active}')

restaurant_pizza_suprema = Restaurant('Pizza Suprema', 'Pizzaria')
restaurant_grao_e_grelha = Restaurant('Grão & Grelha', 'Hamburguer')

Restaurant.list_restaurants()
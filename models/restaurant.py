class Restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        active = False

restaurant_pizza_suprema = Restaurant('Pizza Suprema', 'Pizzaria')
restaurant_grao_e_grelha = Restaurant('Grão & Grelha', 'Hamburguer')

print(vars(restaurant_pizza_suprema))
print(vars(restaurant_grao_e_grelha))
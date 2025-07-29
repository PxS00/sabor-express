class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self) -> str:
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}' )
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}')

    @property
    def active(self): 
        return '⌧' if self._active else '☐'
    
    def toggle_state(self):
        self._active = not self._active
 
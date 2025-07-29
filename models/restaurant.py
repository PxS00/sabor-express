from models.rating import Rating

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._rating = []
        Restaurant.restaurants.append(self)

    def __str__(self) -> str:
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}' )
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.media_ratings).ljust(25)} | {restaurant.active}')

    @property
    def active(self): 
        return '⌧' if self._active else '☐'
    
    def toggle_state(self):
        self._active = not self._active

    def receive_rating(self, client, grade):
        rating = Rating(client, grade)
        self._rating.append(rating)

    @property
    def media_ratings(self):
        if not self._rating:
            return 0
        sum_of_grades = sum(rating._grade for rating in self._rating)
        number_of_notes = len(self._rating)
        media = round(sum_of_grades / number_of_notes, 1)
        return media
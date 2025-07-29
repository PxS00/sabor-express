from models.rating import Rating
from models.menu.menu_item import MenuItem

class Restaurant:
    """Represents a restaurant and its characteristics."""
    
    restaurants = []

    def __init__(self, name, category):
        """
        Initializes a Restaurant instance.

        Parameters:
        - name (str): The name of the restaurant.
        - category (str): The category of the restaurant.
        """
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self) -> str:
        """Returns a string representation of the restaurant."""
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        """
        Displays a formatted list of all registered restaurants.
        """
        print(f'{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} | {'Status'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.media_ratings).ljust(25)} | {restaurant.active}')

    @property
    def active(self): 
        """
        Returns a symbol indicating the restaurant's active state.

        Returns:
        - str: '⌧' if active, '☐' if inactive.
        """
        return '⌧' if self._active else '☐'
    
    def toggle_state(self):
        """
        Toggles the active state of the restaurant.
        """
        self._active = not self._active

    def receive_rating(self, client, grade):
        """
        Records a new rating for the restaurant.

        Parameters:
        - client (str): The name of the customer who gave the rating.
        - grade (float): The rating given, between 1 and 5.
        """
        if 0 < grade <= 5:
            rating = Rating(client, grade)
            self._rating.append(rating)

    @property
    def media_ratings(self):
        """
        Calculates and returns the average rating for the restaurant.

        Returns:
        - float or str: The average rating rounded to 1 decimal, or '-' if no ratings exist.
        """
        if not self._rating:
            return '-'
        sum_of_grades = sum(rating._grade for rating in self._rating)
        number_of_notes = len(self._rating)
        media = round(sum_of_grades / number_of_notes, 1)
        return media

    def add_to_menu(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)

    @property
    def show_menu(self):
        print(f'\nCardápio do restaurante {self._name}\n')

        for i, item in enumerate(self._menu, start=1):
            detalhes = [f'{i}. Nome: {item._name}', f'Preço: R${item._price:.2f}']

            if hasattr(item, 'size'):
                detalhes.append(f'Tamanho: {item.size}')
            if hasattr(item, 'description'):
                detalhes.append(f'Descrição: {item.description}')
            if hasattr(item, 'type'):
                detalhes.append(f'Tipo: {item.type}')

            print(' | '.join(detalhes))
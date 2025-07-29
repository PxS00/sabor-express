from models.menu.menu_item import MenuItem

class Dessert(MenuItem):
    def __init__(self, name, price, type, size, description):
        super().__init__(name, price)
        self.type = type
        self.size = size
        self.description = description

    def __str__(self) -> str:
        return self._name
    
    def apply_discount(self):
        pass

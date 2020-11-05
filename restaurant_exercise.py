# Create a parent class named menu which has its specific attributes

class Menu:

    def __init__(self):
        self.menu = [
            "Chips",
            "BBQ Wings",
            "Spicy Wings",
            "Pizza",
            "Dono's Burger Meal",
            "Seabass",
            "Fish and Chips",
            "Sunday Roast"
        ]

# Create a child class for the waiter

class Waiter(menu):

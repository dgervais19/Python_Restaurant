# Create a parent class named menu which has its specific attributes

class Menu:
# Initialise the class
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


class Waiter(Menu):

    def __init__(self):
        # Inherit attributes from the parent class
        super().__init__()

# Create the function that allows the user to make an order
    def order_process(self):

        order = []  # Assign an empty list to the variable "order"

        print("What would you like to eat today?")

# Create a while loop that breaks once the length of the list is > 3
        while len(order) < 3:
            choice = input("Order Here ==> ")
            if choice in self.menu:
                order.append(choice)
            else:
                print("Sorry, this is not in the menu")
            if len(order) < 3:
                choice_2 = input("Would you like anything else?(Y/N) ")
                if choice_2[0] in ["n", "N"]:
                    break

        return order


if __name__ == "__main__":
    user = Waiter()
    print(user.menu)
    order_list = user.order_process()
    print(f"Here is your order:\n{order_list}")



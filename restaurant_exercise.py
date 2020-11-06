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
            if choice in self.menu:  # Add the choice to the list if it is part of the menu
                order.append(choice)
            else:
                print("Sorry, this is not in the menu")

            if len(order) < 3: # An if condition that asks if the user would like to order again
                choice_2 = input("Would you like anything else?(Y/N) ")

                # Also break loop if the user doesn't want to pick anything else
                if choice_2[0] in ["n", "N"]:
                    break

        return order


if __name__ == "__main__": # if we are on this file then run whats under the if statement
    user = Waiter() # Create an object to assign the attributes of the parent class "Waiter()"
    print(user.menu)
    order_list = user.order_process()  # assigning the returned value in the order_process function to a variable
    print(f"Here is your order:\n{order_list}")



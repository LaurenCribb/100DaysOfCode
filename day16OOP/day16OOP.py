# Importing the turtle class and using it to move around the screen
#
#
#
# import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
#
#

# Installing and importing PrettyTable to use the module and make a table
#
#
#
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)
#
#
#

# Making the coffee machine again using OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
working = True

while working == True:
    order_name = input(f"What would you like? ({menu.get_items()}): ")
    if order_name == "off":
        working = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_object = menu.find_drink(order_name)
        can_be_made = coffee_maker.is_resource_sufficient(drink_object)
        if can_be_made:
            payment = money_machine.make_payment(drink_object.cost)
            if payment:
                make_order = coffee_maker.make_coffee(drink_object)

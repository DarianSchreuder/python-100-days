from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while True:

    options = menu.get_items()
    user_decision = input(f"What would you like? ({options}): ")

    if user_decision == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_decision == "off":
        print("powering down...")
        break
    else:
        drink = menu.find_drink(user_decision)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

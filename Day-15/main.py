MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def dispense_drink(drink):
    print(f"Here is your {drink}. Enjoy!")
    return MENU[str(drink)]["cost"]


def check_transaction(total, drink):
    if float(total) < float(MENU[str(drink)]["cost"]):

        return print("Sorry that's not enough money. Money refunded.")

    else:

        total -= MENU[str(drink)]["cost"]
        print(f"Here is ${total}")

    if drink == "espresso":

        resources['water'] -= MENU[str(drink)]["ingredients"]['water']
        resources['coffee'] -= MENU[str(drink)]["ingredients"]['coffee']

    else:

        for key in resources:
            resources[key] -= MENU[str(drink)]["ingredients"][key]

    return True


def request_payment(drink):
    quaters = int(input("Insert quaters($0.25): "))
    dimes = int(input("Insert dimes($0.10): "))
    nickels = int(input("Insert pennies($0.01): "))

    total = float(quaters * 0.25 + dimes * 0.10 + nickels * 0.01)

    return check_transaction(total, drink)


def check_resources(drink):
    if drink != "espresso":

        for key in resources:

            if int(resources[key]) < int(MENU[str(drink)]["ingredients"][key]):
                return print(f"Insufficient {key}: {resources[key]}")

    else:
        if int(resources["coffee"]) < int(MENU[str(drink)]["ingredients"]["coffee"]):
            return print(f"Insufficient coffee: {resources['coffee']}")

        if int(resources["water"]) < int(MENU[str(drink)]["ingredients"]["water"]):
            return print(f"Insufficient water: {resources['water']}")

    return request_payment(drink)


while True:

    user_decision = str(input("What would you like? (espresso/latte/cappuccino):"))



    match user_decision.lower():

        case "espresso":

            is_valid = check_resources("espresso")
            if is_valid:
                money += dispense_drink(user_decision)
        case "latte":

            is_valid = check_resources("latte")
            if is_valid:
                money += dispense_drink(user_decision)
        case "cappuccino":

            is_valid = check_resources("cappuccino")
            if is_valid:
                money += dispense_drink(user_decision)
        case "report":

            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")

        case "off":

            print("Powering Down")
            break

        case _:

            print("invalid choice")

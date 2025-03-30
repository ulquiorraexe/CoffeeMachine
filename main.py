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
profit = 0

def check_item(car):
    for item in car:
        if car[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def coin_say():
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def return_money(received, cost):
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, not enough money.")
        return False

def make_coffee(name, car):
    for item in car:
        resources[item] -= car[item]
    print(f"Here is {name}, bon appétit!")

open = True
while open:
    cof = input("What would you like? (espresso/latte/cappuccino) ")
    if cof == "off":
        open = False
    elif cof == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
    else:
        drink = MENU[cof]
        if check_item(drink["ingredients"]):
            payment = coin_say()
            if return_money(payment, drink["cost"]):
                make_coffee(cof, drink["ingredients"])

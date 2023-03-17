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

total_cash = 0


# Function which makes espresso and deducts ingredients from resources dictionary
def make_espresso(espresso):
    cup_of_coffee = MENU[espresso]
    water = cup_of_coffee['ingredients']['water']
    coffee = cup_of_coffee['ingredients']['coffee']
    resources['coffee'] -= coffee
    resources['water'] -= water
    return print("Here is your espresso ☕️. Enjoy!")


# Function which makes cappuccino and deducts ingredients from resources dictionary
def make_cappuccino(cappuccino):
    cup_of_coffee = MENU[cappuccino]
    water = cup_of_coffee['ingredients']['water']
    milk = cup_of_coffee['ingredients']['milk']
    coffee = cup_of_coffee['ingredients']['coffee']
    resources['coffee'] -= coffee
    resources['milk'] -= milk
    resources['water'] -= water
    return print("Here is your cappuccino ☕️. Enjoy!")


# Function which makes latte and deducts ingredients from resources dictionary
def make_latte(latte):
    cup_of_coffee = MENU[latte]
    water = cup_of_coffee['ingredients']['water']
    milk = cup_of_coffee['ingredients']['milk']
    coffee = cup_of_coffee['ingredients']['coffee']
    resources['coffee'] -= coffee
    resources['milk'] -= milk
    resources['water'] -= water
    return print("Here is your latte ☕️. Enjoy!")


# Function which returns change
def change_giver(cash, coffee_type):
    if coffee_type == 'espresso':
        change = cash - 1.5
        change = round(change, 2)
        return change
    elif coffee_type == 'latte':
        change = cash - 2.5
        change = round(change, 2)
        return change
    elif coffee_type == 'cappuccino':
        change = cash - 3.0
        change = round(change, 2)
        return change


# Sum of all coins
def sum_of_coins(quarter, dime, nickle, penny):
    total = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
    total = round(total, 2)
    return total


while True:
    # Here user chooses which coffee should be made by coffee machine
    prompt = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${total_cash}")
    elif prompt == 'off':
        break
    elif prompt == 'latte':
        # First we check whether enough ingredients or not
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                    # If there are enough ingredients to make coffee, then we ask to pay
                    print("Please insert coins.")
                    quarters = int(input("how many quarters?: "))
                    dimes = int(input("how many dimes?: "))
                    nickles = int(input("how many nickles?: "))
                    pennies = int(input("how many pennies?: "))
                    total = sum_of_coins(quarters, dimes, nickles, pennies)
                    if total >= 2.5:
                        change = change_giver(total, prompt)
                        make_latte(prompt)
                        total_cash += 2.5
                        print(f"Here is ${change} in change.")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                # If there are not enough ingredients, we print the line below
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")

    elif prompt == 'cappuccino':
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                    print("Please insert coins.")
                    quarters = int(input("how many quarters?: "))
                    dimes = int(input("how many dimes?: "))
                    nickles = int(input("how many nickles?: "))
                    pennies = int(input("how many pennies?: "))
                    total = sum_of_coins(quarters, dimes, nickles, pennies)
                    if total >= 3.0:
                        change = change_giver(total, prompt)
                        make_cappuccino(prompt)
                        total_cash += 3.0
                        print(f"Here is ${change} in change.")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")

    elif prompt == 'espresso':
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickles = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))
                total = sum_of_coins(quarters, dimes, nickles, pennies)
                if total >= 1.5:
                    change = change_giver(total, prompt)
                    make_espresso(prompt)
                    total_cash += 1.5
                    print(f"Here is ${change} in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    else:
        print("You did spelling mistake. Reenter again. Or if you want to close coffee machine, type 'off'")

# To stop the code type "off", to see the report about coffee machine type "report"

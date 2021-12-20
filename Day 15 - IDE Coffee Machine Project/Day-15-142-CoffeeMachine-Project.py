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
    "money": 0,
}

PowerOff = False


def coffee_machine(drink):
    def cost(drink):
        quarters = 0.25
        dimes = 0.10
        nickels = 0.05
        pennies = 0.01

        # print(MENU[drink]["cost"]) #  Debugging
        drink_cost = MENU[drink]["cost"]
        resources['money'] += drink_cost
        print(f'That will be ${drink_cost}')
        quarters_amount = float(input('How many quarters?: '))
        quarters_total = quarters * quarters_amount
        # print(quarters_total) #  Debugging
        dimes_amount = float(input('How many dimes?: '))
        dimes_total = dimes * dimes_amount
        # print(dimes_total) #  Debugging
        nickels_amount = float(input('How many nickels?: '))
        nickel_total = nickels * nickels_amount
        # print(nickel_total) #  Debugging
        pennies_amount = float(input('How many pennies?: '))
        pennies_total = pennies * pennies_amount
        # print(pennies_total) #  Debugging
        total = (quarters_total + dimes_total + nickel_total + pennies_total)
        # print(total) #  Debugging
        if total > float(drink_cost):
            print(f"Your remainder is: ${round(total - drink_cost, 2)}")
            print(f"Heh, heh... Enjoy your {drink} ☕, stranger!")
            resource = resources['water'] = water_remainder
            resource = resources['coffee'] = coffee_remainder
            if drink != 'espresso':
                resource = resources['milk'] = milk_remainder

        elif float(drink_cost) > total:
            print("Sorry, that's not enough cash, stranger!")
            print(f"You need ${round(drink_cost - total, 2)} more!")

    """Checks the resource of the product"""

    cost_water = MENU[drink]["ingredients"]['water']
    cost_coffee = MENU[drink]["ingredients"]['coffee']
    if drink != 'espresso':
        cost_milk = MENU[drink]["ingredients"]['milk']
    if drink == 'latte':
        if (resources['water'] - cost_water) >= 0 and (resources['water'] - cost_milk) >= 0 and (
                resources['water'] - cost_coffee) >= 0:
            water_remainder = (resources['water'] - cost_water)
            # print(f'Water remaining: {water_remainder}') #  Debugging
            coffee_remainder = (resources['coffee'] - cost_coffee)
            # print(f'Coffee Remaining: {coffee_remainder}') #  Debugging
            milk_remainder = (resources['milk'] - cost_milk)
            # print(f'Milk Remaining: {milk_remainder}') #  Debugging
            cost(drink)
        elif (resources['water'] - cost_water) < 0 or (resources['coffee'] - cost_coffee) < 0 or (
                resources['milk'] - cost_milk) < 0:
            print(f"Not enough resource, stranger!")
    elif drink == 'espresso':
        if (resources['water'] - cost_water) >= 0 and (resources['water'] - cost_coffee) >= 0:
            water_remainder = (resources['water'] - cost_water)
            # print(f'Water remaining: {water_remainder}') #  Debugging
            coffee_remainder = (resources['coffee'] - cost_coffee)
            # print(f'Coffee Remaining: {coffee_remainder}') #  Debugging
            cost(drink)
        elif (resources['water'] - cost_water) < 0 or (resources['coffee'] - cost_coffee) < 0:
            print(f"Not enough resource, stranger!")
    elif drink == 'cappuccino':
        if (resources['water'] - cost_water) >= 0 and (resources['water'] - cost_milk) >= 0 and (
                resources['water'] - cost_coffee) >= 0:
            water_remainder = (resources['water'] - cost_water)
            # print(f'Water remaining: {water_remainder}') #  Debugging
            coffee_remainder = (resources['coffee'] - cost_coffee)
            # print(f'Coffee Remaining: {coffee_remainder}') #  Debugging
            milk_remainder = (resources['milk'] - cost_milk)
            # print(f'Milk Remaining: {milk_remainder}') #  Debugging
            cost(drink)
        elif (resources['water'] - cost_water) < 0 or (resources['coffee'] - cost_coffee) < 0 or (
                (resources['milk'] - cost_milk) < 0 and not drink == 'espresso'):
            print(f"Not enough resource, stranger!")
    else:
        print("Error typing, try again!")


def report():
    """
    :return: For reporting the amount of resources currently
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# report() #  Debugging


while not PowerOff:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'latte' or drink == 'espresso' or drink == 'cappuccino':
        coffee_machine(drink)
    elif drink == 'report':
        report()
    elif drink == 'off':
        PowerOff = True
        print("Machine entering maintenance mode")
    else:
        print("Error typing, try again")

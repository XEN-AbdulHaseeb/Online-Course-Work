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
    "water": 30000,
    "milk": 20000,
    "coffee": 10000,
}
money = 0


def resources_sufficient():
    global resources
    if resources['water'] >= 50 and resources['coffee'] >= 18:  # Can at least provide Espresso
        return True
    else:
        print('Insufficient Resources, OUT OF ORDER')
        return False


def dispense(choice, choice_string):
    global resources, MENU, money
    change = 0
    print('Please insert coins UwU')
    quarter = int(input('Insert Quarters: '))
    dimes = int(input('Insert Dimes: '))
    nickels = int(input('Insert Nickels: '))
    pennies = int(input('Insert Pennies: '))
    total = .25 * quarter + .1 * dimes + .05 * nickels + .01 * pennies
    cost = choice['cost']

    if total < cost:
        print('Insufficient funds!\nTransaction aborted!')
    else:
        change = total - cost
        change = round(change, 2)  # Computers have trouble handling floating point arithmetic
        money += cost
        resources['water'] -= choice['ingredients']['water']
        resources['coffee'] -= choice['ingredients']['coffee']
        if choice_string != 'espresso':
            resources['milk'] -= choice['ingredients']['milk']
        if change != 0:
            print(f'Here is your ${change} in change')
        print(f'Enjoy your {choice_string}')
        # print(resources['water'], resources['coffee'], resources['milk'])


while resources_sufficient():
    choice = input('What would you like? (espresso/latte/cappuccino): ')

    if choice != 'espresso' and choice != 'latte' and choice != 'cappuccino' and choice != 'report' and choice != 'off':
        print('Invalid choice!')
        continue
    if choice == 'off':
        exit()

    if choice == 'report':
        print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {money}')
    elif MENU[choice]['ingredients']['water'] > resources['water'] \
            or (choice != 'espresso' and MENU[choice]['ingredients']['milk'] > resources['milk']) \
            or MENU[choice]['ingredients']['coffee'] > resources['coffee']:
        # The conditions are read from left to right, for AND operation if left most condition is false it won't
        # bother checking the rest,for the second condition if choice isn't espresso it won't bother with checking
        # milk resource, which fixes KeyError as milk isn't a valid key for espresso, a simple fix would be to just
        # add milk to espresso and give it 0 requirements, but that's boring :P
        print('Sorry not enough resources.')
    else:
        dispense(MENU[choice], choice)
print('Insufficient resources, OUT OF ORDER')

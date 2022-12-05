from menu import MENU


def check_resources(coffee):
    ingredients = MENU[f'{coffee}']['ingredients']
    if resources['water'] >= ingredients['water'] and \
            resources['coffee'] >= ingredients['coffee'] and \
            resources['milk'] >= ingredients['milk']:
        return True
    else:
        return False


def process_coin(pen, nic, dim, qua):
    pennies_value = pen * 0.1
    nickles_value = nic * 0.1
    dimes_value = dim * 0.1
    quarter_value = qua * 0.1
    total = pennies_value + nickles_value + dimes_value + quarter_value
    return total


def check_value(coffee, val):
    print(val)
    cost = MENU[coffee]['cost']
    print(cost)
    if val >= cost:
        return True
    else:
        return False


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choice = input('What yould you like ("espresso", "latte", "cappuccino")'
               ).lower()

if choice == 'off':
    exit()
elif choice == 'report':
    print(resources)
elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
    has_resources = check_resources(choice)
    if has_resources:
        pennies = int(input('How many pennies: '))
        nickles = int(input('How many nickles : '))
        dimes = int(input('How many dimes : '))
        quarter = int(input('How many quarters: '))
        value = process_coin(pennies, nickles, dimes, quarter)
        enough_money = check_value(choice, value)
        if enough_money:
            print('Here is your coffee')
            # TODO: make a change system
        else:
            print('You do not have enough money. Money refunded')
    else:
        print('Sorry we do not have enough ingredient for this coffee')
else:
    print('error')

# TODO: Make it a loop
# TODO: Deduct ingredients

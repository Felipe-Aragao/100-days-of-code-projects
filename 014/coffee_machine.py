from menu import MENU


def check_resources(coffee):
    ingredients = MENU[f'{coffee}']['ingredients']
    if (resources['water'] >= ingredients['water'] and
            resources['coffee'] >= ingredients['coffee'] and
            resources['milk'] >= ingredients['milk']):
        return True
    else:
        return False


def process_coin(pen, nic, dim, qua):
    pennies_value = pen * 0.1
    nickles_value = nic * 0.1
    dimes_value = dim * 0.1
    quarter_value = qua * 0.1
    total = pennies_value + nickles_value + dimes_value + quarter_value
    return f'{total:.2f}'


def check_value(coffee, val):
    coffee_cost = MENU[coffee]['cost']
    if val >= coffee_cost:
        return True
    else:
        return False


def use_ingredients(coffee):
    ingredients = MENU[f'{coffee}']['ingredients']
    for n in resources:
        resources[n] -= ingredients[n]


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

while True:
    choice = input('What yould you like ("espresso", "latte", "cappuccino")'
                   ).lower()

    if choice == 'off':
        break
    elif choice == 'report':
        for i in resources:
            print(f'{i.title()} = {resources[i]}')
        print(f'Profit = {profit}')
        continue
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        has_resources = check_resources(choice)
        if has_resources:
            pennies = int(input('How many pennies: '))
            nickles = int(input('How many nickles : '))
            dimes = int(input('How many dimes : '))
            quarter = int(input('How many quarters: '))
            value = float(process_coin(pennies, nickles, dimes, quarter))
            enough_money = check_value(choice, value)
            cost = MENU[choice]["cost"]
            if enough_money:
                print(f'Here is your change: ${value - cost}')
                profit += cost
                print(f'\nHere is your {choice.title()}!')
                use_ingredients(choice)
                continue
            else:
                print('You do not have enough money. Money refunded')
                continue
        else:
            print('Sorry we do not have enough ingredient for this coffee')
            continue
    else:
        print('Invalid option')
        continue

print('\nOFF')

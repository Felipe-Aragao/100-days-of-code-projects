import os


def participants():
    while True:
        participant = input('Is there any other bidders? (Y)(N)').lower()
        if participant[0] == 'y':
            return True
        elif participant[0] == 'n':
            return False
        else:
            continue


def profile():
    name = input('Name: ')
    bid = float(input('Bid: $'))
    bidders[name] = bid
    return bidders


bidders = {}
win_price = 0
win_name = ''

print('Welcome to secret auction')

profile()
while participants():
    os.system('cls')
    profile()

for i in bidders:
    if bidders[i] > win_price:
        win_price = bidders[i]
        win_name = i

print(f'The winner is {win_name} with ${win_price}')

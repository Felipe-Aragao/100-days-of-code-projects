import random


def lose_msg():
    print(f'\nYour final cards: {player_cards}, Final score: {player_sum}')
    print('YOU LOSE!')
    print(
        f'Computer final cards: {computer_cards}, Final score: {computer_sum}')


def win_msg():
    print(f'\nYour final cards: {player_cards}, Final score: {player_sum}')
    print('YOU WIN!')
    print(
        f'Computer final cards: {computer_cards}, Final score: {computer_sum}')


continue_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
for i in range(0, 2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
player_sum = 0
computer_sum = 0
print('BLACKJACK')

while continue_game:
    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)

    print(f'\nYour cards: {player_cards}, Current score: {player_sum}')
    print(f'Computer first card: {computer_cards[0]}')
    print(f'{computer_cards}===={computer_sum}')  # Debug

    if player_sum > 21 or computer_sum > 21:
        break

    hit = input('\nPick up another card?(Y/N)').lower()
    if hit[0] == 'y':
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    elif hit[0] == 'n':
        continue_game = False
    else:
        print('Please, chose a valid option.')
        continue

if player_sum > 21:  # More than 21
    lose_msg()
elif computer_sum > 21:  # More than 21
    win_msg()
elif player_sum < computer_sum:  # Computer closer to 21
    lose_msg()
elif player_sum > computer_sum:  # Computer closer to 21
    win_msg()

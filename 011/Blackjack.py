import random
import os


def lose_msg():
    print(f'\nYour final cards: {player_cards}, Final score: {player_sum}')
    print('YOU LOSE!')
    print(
        f'Computer final cards: {computer_cards}, Final score: {computer_sum}\n')


def win_msg():
    print(f'\nYour final cards: {player_cards}, Final score: {player_sum}')
    print('YOU WIN!')
    print(
        f'Computer final cards: {computer_cards}, Final score: {computer_sum}\n')


def draw_msg():
    print(f'\nYour final cards: {player_cards}, Final score: {player_sum}')
    print(
        f'Computer final cards: {computer_cards}, Final score: {computer_sum}\n')
    print('DRAW')


def game():
    global player_sum, computer_sum
    continue_game = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(0, 2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    print('BLACKJACK')

    while continue_game:
        player_sum = sum(player_cards)
        computer_sum = sum(computer_cards)

        if player_sum > 21 and 11 in player_cards:
            index = player_cards.index(11)
            player_cards[index] = 1
            player_sum = sum(player_cards)
        if computer_sum > 21 and 11 in player_cards:
            index = computer_cards.index(11)
            computer_cards[index] = 1
            computer_sum = sum(computer_cards)
        if player_sum > 21 or computer_sum > 21:
            break

        print(f'\nYour cards: {player_cards}, Current score: {player_sum}')
        print(f'Computer first card: {computer_cards[0]}')

        hit = input('\nPick up another card?(Y/N)').lower()
        if hit[0] == 'y':
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        elif hit[0] == 'n':
            continue_game = False
        else:
            print('Please, chose a valid option.')
            continue

    if player_sum == computer_sum:
        draw_msg()
    elif player_sum > 21:  # More than 21
        lose_msg()
    elif computer_sum > 21:  # More than 21
        win_msg()
    elif player_sum < computer_sum:  # Computer closer to 21
        lose_msg()
    elif player_sum > computer_sum:  # Computer closer to 21
        win_msg()
    new_game = input('Play another game of blackjack?(Y/N)\n').lower()
    if new_game[0] == 'y':
        player_cards.clear()
        computer_cards.clear()
        player_sum = 0
        computer_sum = 0
        os.system('cls')
        game()


player_cards = []
computer_cards = []
player_sum = 0
computer_sum = 0
game()

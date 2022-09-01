import random


options = ['rock', 'paper', 'scissor']
choice = input('Chose "Rock" "Paper" or "Scissor": ').lower()
index_user_option = 0

try:
    index_user_option = int(options.index(choice))
except ValueError:
    print('ERROR')
    exit()

random_option = random.randint(0, 2)
computer_choice = options[random_option]

print(f'You chose {choice.swapcase()}')
print(f'Computer chose {computer_choice.swapcase()}\n')

if index_user_option == 0 and random_option == 2:
    print("You win!")
elif random_option == 0 and index_user_option == 2:
    print("You lose")
elif random_option > index_user_option:
    print("You lose")
elif index_user_option > random_option:
    print("You win!")
elif random_option == index_user_option:
    print("It's a draw")


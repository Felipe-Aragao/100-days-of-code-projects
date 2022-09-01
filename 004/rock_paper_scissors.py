import random

options = ['rock', 'paper', 'scissor']
choice = input('Chose "Rock" "Paper" or "Scissor": ').lower()
index_user_option = 0

try:
    index_user_option = options.index(choice)
except ValueError:
    print('ERROR')
    exit()

computer_choice = random.randint(0, 2)
computer_choice_str = options[computer_choice]

print(f'You chose {choice.swapcase()}')
print(f'Computer chose {computer_choice_str.swapcase()}\n')

if index_user_option == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and index_user_option == 2:
    print("You lose")
elif computer_choice > index_user_option:
    print("You lose")
elif index_user_option > computer_choice:
    print("You win!")
elif computer_choice == index_user_option:
    print("It's a draw")

import random


options = ['rock', 'paper', 'scissor']

choice = input('Chose "Rock" "Paper" or "Scissor": ').lower()

random_option = random.randint(0, 2)
computer_choice = options[random_option]

if choice == 'rock' or choice == 'paper' or choice == 'scissor':
    print(f'You chose {choice.swapcase()}')
    print(f'Computer chose {computer_choice.swapcase()}\n')
else:
    print('ERROR')

if computer_choice == choice:
    print('Draw')
elif computer_choice == 'rock' and choice == 'scissor':
    print('You lose!')
elif computer_choice == 'paper' and choice == 'rock':
    print('You lose!')
elif computer_choice == 'scissor' and choice == 'paper':
    print('You lose!')
elif choice == 'rock' and computer_choice == 'scissor':
    print('You win!')
elif choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif choice == 'scissor' and computer_choice == 'paper':
    print('You win!')

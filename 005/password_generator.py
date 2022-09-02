import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
    , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C'
    , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'
    , 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input('How many letters do you want in your password? '))
num_numbers = int(input('How many numbers? '))
num_symbols = int(input('How many symbols? '))

password_character = []
for i in range(0, num_letters):
    password_character.append(random.choice(letters))
for i in range(0, num_numbers):
    password_character.append(random.choice(numbers))
for i in range(0, num_symbols):
    password_character.append(random.choice(symbols))

password = ''
for character in password_character[::-1]:
    password = character + password

print(f'Your password is: {password}')

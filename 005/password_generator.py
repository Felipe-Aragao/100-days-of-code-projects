import random

password = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
    , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C'
    , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'
    , 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_letters = int(input('How many letters do you want in your password? '))
number_numbers = int(input('How many numbers? '))
number_symbols = int(input('How many symbols? '))

password_characters = []
for i in range(0, number_letters):
    password_characters.append(random.choice(letters))
for i in range(0, number_numbers):
    password_characters.append(random.choice(numbers))
for i in range(0, number_symbols):
    password_characters.append(random.choice(symbols))

random.shuffle(password_characters)
for character in password_characters[::-1]:
    password += character

print(f'Your password is: {password}')

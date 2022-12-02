import random

attempts = 0
while True:
    difficulty = str(input('Chose a difficulty: "Easy" or "Hard": ')).lower()
    if difficulty == 'easy':
        attempts = 10
        break
    elif difficulty == 'hard':
        attempts = 5
        break
    else:
        print('Chose a valid difficulty')
        continue

random_number = random.randint(1, 100)
while True:
    print(f'\nYou have {attempts} attempts to guess a number between 1 - 100')
    guess = int(input('Make a Guess: '))
    print(random_number)

    if guess == random_number:
        print('\nCorrect')
        print(f'You finished the game with {attempts - 1} attempts remaining')
        break
    if attempts == 1:
        print("\nYou've run out of guesses, you lose.")
        print(f'The answer was {random_number}')
        break

    if guess <= 0 or guess > 100:
        print('\nChose a number between 1 - 100')
    elif guess > random_number:
        print('\nToo high')
        attempts -= 1
    elif guess < random_number:
        print('\nToo low')
        attempts -= 1

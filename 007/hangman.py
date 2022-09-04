import random

# Create initial variables and lists
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
display = list('_' * len(chosen_word))
lives = 5
# Debug print()
print(chosen_word)
print('Welcome to Hangman game! You have 5 lives to complete')

while '_' in display and lives > 0:
    # Ask for a letter to the user
    guess = str(input('Choose a letter: ')).lower()
    # Start a loop in the length of the word to see if the letter is in
    # more than one position
    for i in range(0, len(chosen_word) - 1):
        if guess in chosen_word_list:
            try:
                index = chosen_word_list.index(guess, i)
            except ValueError:
                continue
            display[index] = guess
            print(''.join(display))
        else:
            print(''.join(display))
            lives -= 1
            if lives == 0:
                print('GAME OVER')
                break
            print(f'{lives} lives remaining')
            break
print(display)

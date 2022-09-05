import random
import hangman_stages as stage  # Drawings of the stickman
import word_list as wl # Word list

# Create initial variables and lists
word_list = wl.word_list
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
display = list('_' * len(chosen_word))
lives = 7
index_stage = 6

# Print introduction to the game
print(f'Welcome to Hangman game! You have {lives} lives to complete')
print(f'{len(chosen_word)} letters\n', ''.join(display))
# Start the game loop that should continue
# while there is blank spaces and while there is still lives
while '_' in display and lives > 0:
    guess = str(input('Choose a letter: ')).lower()
    # Test if the guess is correct
    for i in range(0, len(chosen_word) - 1):
        if guess in chosen_word_list:
            try:
                index = chosen_word_list.index(guess, i)
            except ValueError:
                continue
            display[index] = guess
        # If the guess is incorrect lose a life
        else:
            index_stage -= 1
            lives -= 1
            # When lives reach 0 it is game over
            if lives == 0:
                print('\nGAME OVER')
                print(f'The correct word was {chosen_word.upper()}')
                break
            print(f'{lives} lives remaining')
            break
    print(f'You guessed {guess}')
    print('\n', ''.join(display))
    if lives > 0:
        print(stage.stages[index_stage], '\n')
# See if the user guessed all letters
if '_' not in display:
    print('Congratulation you WON!')

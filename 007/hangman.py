import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = list('_' * len(chosen_word))
chosen_word_list = list(chosen_word)
print(chosen_word)

guess = str(input('Choose a letter: ')).lower()
for i in range(0, len(chosen_word) - 1):
    if guess in chosen_word_list:
        try:
            index = chosen_word_list.index(guess, i)
        except ValueError:
            continue
        i += 1
        display[index] = guess
    else:
        print('Wrong!')
        break
print(display)
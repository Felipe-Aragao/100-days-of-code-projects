import random
from game_data import data


def person_characteristics():
    random_number = random.randint(0, len(data) - 1)
    name = data[random_number]['name']
    follower_count = data[random_number]['follower_count']
    description = data[random_number]['description']
    country = data[random_number]['country']
    vowels = {'A', 'E', 'I', 'O', 'U'}
    if description[0] in vowels:
        print(f'{name}, an {description} from {country}')
    else:
        print(f'{name}, a {description} from {country}')
    return follower_count, name


def win_condition(follow_a, follow_b):
    if follow_a[0] > follow_b[0] or followers_a[0] == followers_b[0]:
        print('\nCorrect')
        print(f'{followers_a[1]} has {followers_a[0]}M followers')
        print(f'{followers_b[1]} has {followers_b[0]}M followers')
        return + 1
    else:
        print('\nWrong')
        print(f'{followers_a[1]} has {followers_a[0]}M followers')
        print(f'{followers_b[1]} has {followers_b[0]}M followers')
        return 0


print('Higher or Lower')
points = 0

while True:
    print('\nA:', end=' ')
    followers_a = person_characteristics()
    print('or')
    print('B:', end=' ')
    followers_b = person_characteristics()
    guess = str(input('Who has more followers? (A/B) ')).lower()
    if guess == 'a':
        points += win_condition(followers_a, followers_b)
        print(f'Points = {points}')
    elif guess == 'b':
        points += win_condition(followers_b, followers_a)
        print(f'Points = {points}')
    else:
        print('Please type a valid option')
        continue

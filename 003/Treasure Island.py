print('Welcome to Treasure Island. Your mission is to find the treasure')
option1 = input('Do you want to go right(r) or left(l)? ').lower()

if option1 == 'l' or option1 == 'left':
    print('You fell into a hole.\nGAME OVER')
elif option1 == 'r' or option1 == 'right':
    option2 = input('You come to a river and you need to cross it, do you'
                    ' swim(s) or do you wait(w)?').lower()
    if option2 == 's' or option2 == 'swim':
        print('You were attacked by an alligator.\nGAME OVER')
    elif option2 == 'w' or option2 == 'wait':
        print('A boat that was passing by helped you cross the river.')
        option3 = input('You see three doors, witch one do you choose to open?'
                        'Red(r),Yellow(y) or Blue(b)').lower()
        if option3 == 'r' or option3 == 'red':
            print('You found lava and burned.\nGAME OVER')
        elif option3 == 'y' or option3 == 'yellow':
            print('Congratulation! YOU WON')
        elif option3 == 'b' or option3 == 'blue':
            print('You found a bear.\nGAME OVER')
        else:
            print('You need to type the correct input option')
    else:
        print('You need to type the correct input option')
else:
    print('You need to type the correct input option')

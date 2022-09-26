from alphabet import alphabet


def caesar(txt, shift, direction):
    new_msg_list = []
    for i in txt:
        try:
            index = alphabet.index(i)
        except ValueError:
            new_msg_list.append(' ')
            continue
        if shift + index <= 25:
            if direction == 'encode':
                new_msg_list.append(alphabet[index + shift])
            else:
                new_msg_list.append(alphabet[index - shift])
        else:
            if direction == 'encode':
                new_shift = shift - (25 - index)
                index = 0
                new_msg_list.append(alphabet[(index + new_shift) - 1])
            else:
                new_shift = shift + (25 - index)
                index = 25
                new_msg_list.append(alphabet[(index - new_shift)])
    new_msg = ''.join(new_msg_list)
    print(new_msg)


def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to "
                          "decrypt:\n")
        if direction != 'encode' and direction != 'decode':
            print('Please choose one option!')
            continue
        else:
            break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift %= 26
    caesar(text, shift, direction)
    repeat = str(input('Repeat? (Yes)(No)\n')).lower()
    if repeat == 'yes':
        main()


main()

def encrypt(txt, shift):
    new_msg_list = []
    for i in txt:
        try:
            index = alphabet.index(i)
        except ValueError:
            new_msg_list.append(' ')
            continue
        if shift + index <= 25:
            new_msg_list.append(alphabet[index + shift])
        else:
            new_shift = shift - (25 - index)
            index = 0
            new_msg_list.append(alphabet[(index + new_shift) - 1])
    new_msg = ''.join(new_msg_list)
    print(new_msg)


def decrypt(txt, shift):
    new_msg_list = []
    for i in txt:
        try:
            index = alphabet.index(i)
        except ValueError:
            new_msg_list.append(' ')
            continue
        if shift + index <= 25:
            new_msg_list.append(alphabet[index - shift])
        else:
            new_shift = shift + (25 - index)
            index = 25
            new_msg_list.append(alphabet[(index - new_shift)])
    new_msg = ''.join(new_msg_list)
    print(new_msg)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('Please choose one option!')
        continue
    else:
        break
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)

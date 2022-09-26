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
            if index == 25:
                index = 0
                new_msg_list.append(alphabet[(index + shift) - 1])
            else:
                new_shift = shift - (25 - index)
                index = 0
                new_msg_list.append(alphabet[(index + new_shift) - 1])
    new_msg = ''.join(new_msg_list)
    print(new_msg)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text, shift)

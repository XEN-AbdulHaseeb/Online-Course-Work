alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_consent = 'yes'
def cipher(msg,shift):
    new_msg = ''
    for i in msg:
        if i not in alphabet:
            new_msg += i
        else:
            new_pos = (alphabet.index(i) + shift) % 26
            new_msg += alphabet[new_pos]
    print(new_msg)

while user_consent == 'yes':
    command = input('Enter encode to encrypt or decode to decrypt: ')
    if not(command == 'encode' or command == 'decode'):
        print('Invalid Entry')
    else:
        msg = input('Type your message: ')
        shift = int(input('Enter shift: ')) % 25
        if command == 'encode':
            cipher(msg,shift)
        elif command == 'decode':
            cipher(msg,-shift)
        else:
            print('Invalid Entry')
            continue
        user_consent = input('Wanna go again? type "yes", or press enter to exit ')

def encode(shift, position):
    """This function encodes."""
    new_position = shift + position    # Adds the position(index of the letter) to the shift number to get the new position.
    new_position %= len(alphabet)    # Divides the new position by 25 and uses the remainder as the new position.
    return new_position   # Returns the new position.

def decode(shift, position):
    """This function decodes."""
    new_position = position - shift    # Minuses the position(index of the letter) from the shift number to get the new position.
    return new_position    # Returns the new position.

user_choice = input("Type 'encode' to encrypt, and type decode to 'decrypt'.\n").lower()    # Asks the user if they would like to encode or decode.
message = input(f'Type the message you want to {user_choice}:\n').lower()    # Asks the user for the message they want encoded/ decoded.
shift = int(input('Type the shift number:\n'))   # Asks the user for the shift number

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']   # Alphabet list

if shift >= len(alphabet): # If the shift number is larger than 25, it does shift divided by 25 and the remiander is used as the shift number.
    shift = shift%(len(alphabet-1))
text = ""
for i in message:
    if i in alphabet:
        position = alphabet.index(i)   # Saves index of the letter as its position.

        if user_choice == 'encode':
            new_position = encode(shift, position)   # If the user picked encode, then the message is encoded.
        elif user_choice == 'decode':
            new_position = decode(shift, position)   # If the user picked decode, then the message is encoded.

        nt = alphabet[new_position]   # Saves nt as the alphabet in the encoded or decoded position.
        text += nt    # Saves the text as nt
    else:
        text += i

print(text)   # Prints text

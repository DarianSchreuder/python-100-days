alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def base(text,shift,direction):
    cipher_text = ""
    for char in text:
        position = alphabet.index(char)
        next_position = position
        if (direction == "encode"):
            next_position += shift
        elif (direction == "decode"):
            next_position -= shift
        new_letter = alphabet[next_position]
        cipher_text += new_letter
    print(f"The {direction}d text is {cipher_text}")
            
if (direction == "encode" or direction == "decode"):
    base(text,shift,direction)
else:
    print(f"Invalid direction: {direction}")
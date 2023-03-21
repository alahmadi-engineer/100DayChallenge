from supportFiles.day8art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,n,type):
    
    message = ""
    for letter in text:
        # if not a letter skip the iteration
        if letter not in alphabet:
            message += letter
            continue

        new_index = 0
        letter_index = alphabet.index(letter)
        if type == 'encode':
            new_index = letter_index + n
            while new_index >= len(alphabet):
                new_index -= len(alphabet)
            message += alphabet[new_index]
        elif type == 'decode':
            new_index = letter_index - n
            while new_index < 0:
                new_index += len(alphabet)
            message += alphabet[new_index]


    print('Your {} messsage is {}'.format(type,message))


def main():
    
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)


if __name__ == "__main__":
    iterate = "y"
    while iterate == "y":
        main()
        iterate = input('do you want to run the program again? Y if yes, N if no\n').lower


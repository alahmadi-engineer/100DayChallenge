# build random password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator !')
num_of_letters = int(input('How many letters would you like in your program? '))
num_of_symbols = int(input('How Many Symbols would you like in your program?'))
num_of_numbers = int(input('How many numbers would you like in your program?'))

password = []

for char in range(1,num_of_letters + 1):
    random_letter = random.choice(letters)
    password.append(random.choice(letters))

for symbol in range(1,num_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password.append(random.choice(symbols))

for number in range(1,num_of_numbers + 1):
    random_number = random.choice(numbers)
    password.append(random.choice(numbers))

random.shuffle(password)
New_password = ""

for i in range(len(password)):
    New_password = New_password + password[i]

print('Your New password is {}'.format(New_password))
# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# # Get user input for password length
# length = int(input("Enter the desired length for the password: "))

# # Generate and display the password
# password = generate_password(length)
# print("Generated password:", password)

# import random
# import string
# def generate_passwords(lenght=12):
#     character = string.ascii_letters + string.digits + string.punctuation
#     passwords = ''.join(random.choice(character) for _ in range(lenght))
#     return passwords
# lenght = int(input("Enter lenght of your desired Password: "))
# password = generate_passwords(lenght)
# print("Generated Passwords:",password)

import random
import string

def generat_passwords(lenght=12):
    character = string.ascii_letters + string.ascii.digits + string.punctuation
    passwords = ''.join(random.choice(character) for _ in range(lenght))
    return passwords

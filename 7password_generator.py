import random
import string

def generate_passwords(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
length = int(input("Enter length of your desired Password: "))
password = generate_passwords(length)
print("Generated Password:", password)

import random
import string

length=int(input("Enter The Length of the Password:"))

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = generate_password(length)
print(password)
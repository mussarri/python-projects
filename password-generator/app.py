import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def generate():
    password_length = int(input("How long would you like to your password to be? "))
    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print(f"password is {password}")


generate()
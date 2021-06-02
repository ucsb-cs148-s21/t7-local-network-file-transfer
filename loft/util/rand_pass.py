from random import randint

def generate_random():
    password = ''
    for i in range(0, 6):
        password += str(randint(0,9))
    return password
from random import randrange

def password_generator():
    passwd= ''.join((chr(randrange(33,122))) for rang in range(randrange(12,15)))
    return passwd

print(password_generator())
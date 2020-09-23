import random

char = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'


userpassAmount = input('How many passwords do you want:')

userpassAmount = int(userpassAmount) 

userpassLength = input('Enter password length:')

userpassLength = int(userpassLength)

for p in range(userpassAmount):
    password = ''
    for c in range(userpassLength):
        password += random.choice(char)
    print(password)
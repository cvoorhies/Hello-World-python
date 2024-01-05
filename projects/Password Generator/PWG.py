import random

print('Welcome to you Password Generator')

chars = 'abcdefghijklmnopqurtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!_+-=@#$%^&*()1234567890'

num_PW = input('Amount of passwords to generate: ')
num_PW = int(num_PW)

len_PW = input('Input the length of your password: ')
len_PW = int(len_PW)

print('\nHere are your password(s):')

for pwd in range(num_PW):
    password = ''
    for c in range(len_PW):
        password += random.choice(chars)

    print(password)

input('don\'t forget to write down your passwords in a safe place')
          



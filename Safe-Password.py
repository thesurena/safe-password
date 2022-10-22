import string,random


length = int(input('Enter your number to create a strong password: '))

while True:

    chars = string.ascii_letters + string.digits + '!@#$%&()_/'

    password = ''.join(random.choice(chars) for itemes in range(length))

    print(f'your safe password: {password}')
    
    while True:
        answer = input('do you want another password (Y/n)'.lower())
        if answer == 'y' or answer == 'n':
            break
    if answer == 'n':
        break
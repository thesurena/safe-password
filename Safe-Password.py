import string,random

#Get a number from the user to generate a random password
length = int(input('Enter your number to create a strong password: '))

while True:
    #Generate a random password
    chars = string.ascii_letters + string.digits + '!@#$%&()_/'
    password = ''.join(random.choice(chars) for itemes in range(length))

    #Show a random password to the user
    print(f'your safe password: {password}')
    
    #Create or stop the password creation operation
    while True:
        answer = input('do you want another password (Y/n)'.lower())
        if answer == 'y' or answer == 'n':
            break
    if answer == 'n':
        break

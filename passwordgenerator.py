import random
import string
import sys
try:
    print('------- THIS IS A RANDOM PASSWORD GENERATOR -------\n')
    color = input('Would you like the text be cyan, red or what white?\n-')
    if color == 'cyan' or color == 'Cyan':
        sys.stdout.write("\033[1;36m")
    elif color == 'Red' or color == 'red':
        sys.stdout.write("\033[1;31m")
    choice = input('Type yes if you would like this computer to generate the length of the entire password,\n\ntype no if you want to type in the lengths.\n\n-')
    if choice == 'Yes' or choice == 'yes':
        upp_case = random.randint(3, 10)
        low_case = random.randint(3, 10)
        spec_case = random.randint(3, 10)
        numbers = random.randint(3, 10)
    elif choice == 'no' or choice == 'No':
        upp_case = int(input('How many uppercase letters do you want? \n-'))
        print('')
        low_case = int(input('How many lowercase letters do you want? \n-'))
        print('')
        spec_case = int(input('How many special charactors do you want? \n-'))
        print('')
        numbers = int(input('How many numbers do you want? \n-'))
        print('')
    uppcase = ''
    lowcase = ''
    speccase = ''
    nums = ''
    password = ''
    print('\n \n \n')
    if upp_case == '' or upp_case == 0:
        print('You need at least 1 uppercase letter')
        upp_case = int(input('How many uppercase letters do you want?'))
    elif low_case == '' or low_case == 0:
        print('You need at least 1 lowercase letter')
        low_case = int(input('How many lowcase letters do you want?'))
    elif spec_case == '' or spec_case == 0:
        print('You need at least 1 special charactor')
        spec_case = int(input('How many special charactors do you want? '))
    elif numbers == '' or numbers == 0:
        print('You need at least number')
        numbers = int(input('How many numbers do you want? '))
    elif upp_case + low_case + spec_case + numbers <= 9:
        print('Your password must be atleast 9 charactors long.')
        upp_case = int(input('How many uppercase letters do you want? \n-'))
        print('')
        low_case = int(input('How many lowercase letters do you want? \n-'))
        print('')
        spec_case = int(input('How many special charactors do you want? \n-'))
        print('')
        numbers = int(input('How many numbers do you want? \n-'))
        print('')
    elif upp_case + low_case + spec_case + numbers >= 50:
        print('Your password must be less than 50 charactors long.')
        upp_case = int(input('How many uppercase letters do you want? \n-'))
        print('')
        low_case = int(input('How many lowercase letters do you want? \n-'))
        print('')
        spec_case = int(input('How many special charactors do you want? \n-'))
        print('')
        numbers = int(input('How many numbers do you want? \n-'))
        print('')
        
    a = 0
    b = 0
    c = 0
    d = 0
    w = str(string.digits)
    x = string.ascii_uppercase
    y = string.ascii_lowercase
    z = string.punctuation
    
    while a != upp_case:
        a = a + 1
        uppcase = uppcase + random.choice(x)
    while b != low_case:
        b = b + 1
        lowcase = lowcase + random.choice(y)
    while c != spec_case:
        c = c + 1
        speccase = speccase + random.choice(z)
    while d != numbers:
        d = d + 1
        nums = str(nums) + str(random.choice(w))
    password = uppcase + lowcase + speccase + nums
    pass_length = int(upp_case) + int(low_case) + int(spec_case) + int(numbers)
    print('Your randomly generated password is:\n' + '\n' + password + '\n \nYour password is ' + str(pass_length) + ' Charactors long!')
except:
    print('An error occurred')
    print('Please try again')
    quit()
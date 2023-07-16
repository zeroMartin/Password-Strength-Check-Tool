import time
from termcolor import colored

print('\n')
print(colored('Password recommendation: ', 'blue'))
print(' -> Have at least 12 characters in your password. Longer is always better')
print(' -> For the best security, use upper and lower case letters, numbers and special characters')
print(' -> Regardles of the password you use, always enable multi-factor authentication for any online account')
print('\n')
password = input('Enter password: ')
print('_____________________________________________________')
print('\n')

U = 'U'
L = 'L'
N = 'N'
S = 'S'

def cliTest():

    passed = colored('Passed', 'green')
    failed = colored('Failed', 'red')

    if N in character_type:
        print('Password has numbers? ...', end = '')
        print(passed)
    else:
        print('Password has numbers? ...', end = '')
        print(failed)
    time.sleep(0.5)
    
    if U in character_type:
        print('Password has upper case letters? ...', end = '')
        print(passed)
    else:
        print('Password has upper case letters? ...', end = '')
        print(failed)
    time.sleep(0.5)
    
    if L in character_type:
        print('Password has lower case letters? ...', end = '')
        print(passed)
    else:
        print('Password has lower case letters? ...', end = '')
        print(failed)
    time.sleep(0.5)
    
    if S in character_type:
        print('Password has special characters? ...', end = '')
        print(passed)
    else:
        print('Password has special characters? ...', end = '')
        print(failed)
    time.sleep(0.5)
    
    if password_length >= 8:
        print('Password has more then 8 characters? ...', end = '')
        print(passed)
    else:
        print('Password has more then 8 characters? ...', end = '')
        print(failed)
    print('_____________________________________________________')
    print('\n')
    time.sleep(0.5)
    return

def check_character_type():
    character_type = []

    for character in password:
        if character.isupper() == True and character.islower() == False and character.isalpha() == True and character.isdigit() == False:
            upper_case = 'U'
            character_type.append(upper_case)
        elif character.isupper() == False and character.islower() == True and character.isalpha() == True and character.isdigit() == False:
            lower_case = 'L'
            character_type.append(lower_case)
        elif character.isupper() == False and character.islower() == False and character.isalpha() == False and character.isdigit() == True:
            number = 'N'
            character_type.append(number)
        elif character.isupper() == False and character.islower() == False and character.isalpha() == False and character.isdigit() == False:
            special_character = 'S'
            character_type.append(special_character)
    return character_type

def check_password_length():
    password_length = len(password)
    return password_length

def check_strength():
    # Only numbers in password
    if N in character_type and U not in character_type and L not in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consits only of numbers')

        if password_length < 16:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed.', 'red'))
        elif password_length == 16:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one week')
            print('\n')
            print(colored('Password is weak and failed', 'red'))
        elif password_length >= 17 and password_length <= 18:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is medium strenght', 'yellow'))
        elif password_length >= 19 and password_length <= 20:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one year')
            print('\n')
            print(colored('Password is strong', 'green'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))

    # Only upper case letters in password
    if N not in character_type and U in character_type and L not in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consist only of upper case letters')

        if password_length <= 11:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed.', 'red'))
        elif password_length == 12:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is medium strenght', 'yellow'))
        elif password_length == 13:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one year')
            print('\n')
            print(colored('Password is strong.', 'green'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))

    # Only lower case letters in password
    if N not in character_type and U not in character_type and L in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consist only of lower case letters')

        if password_length <= 11:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed.', 'red'))
        elif password_length == 12:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is medium strenght', 'yellow'))
        elif password_length == 13:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one year')
            print('\n')
            print(colored('Password is strong.', 'green'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))
        
    # Upper and lower case letters in password
    if N not in character_type and U in character_type and L in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consist of upper and lower case letters')

        if password_length <= 9:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed', 'red'))
        elif password_length == 10:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is medium strenght', 'yellow'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))

    # Upper case letters and numbers in password
    if N in character_type and U in character_type and L not in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consist of upper case letters and numbers')

        if password_length <= 9:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed', 'red'))
        elif password_length == 10:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is medium strenght', 'yellow'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))
        
    # Lower case letters and numbers in password
    if N in character_type and U not in character_type and L in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consist of lower case letters and numbers')

        if password_length <= 9:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed', 'red'))
        elif password_length == 10:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is medium strenght', 'yellow'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))
        
    # Numbers, Upper and lower case letters in password
    if N in character_type and U in character_type and L in character_type and S not in character_type:
        print('Password: ', password)
        print(' -> Password consist of numbers, upper and lower case letters')

        if password_length <= 8:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed.', 'red'))
        elif password_length ==9:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one week')
            print('\n')
            print(colored('Password is weak and faild', 'red'))
        elif password_length == 10:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one year')
            print('\n')
            print(colored('Password is strong.', 'green'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))

    # Numbers, Upper and lower case letters and special characters in password
    if N in character_type and U in character_type and L in character_type and S in character_type:
        print('Password: ', password)
        print(' -> Password consist of numbers, upper and lower case letters and special characters')

        if password_length <= 8:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then 24h')
            print('\n')
            print(colored('Password is very weak and failed.', 'red'))
        elif password_length == 9:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Less then one month')
            print('\n')
            print(colored('Password is intermediate strenght', 'yellow'))
        else:
            print(' -> Password lenght: ', len(password))
            print(' -> Estimated time to crack password: Couple of years')
            print('\n')
            print(colored('Password is very strong', 'green'))
    return

character_type = check_character_type()

password_length = check_password_length()

cliTest()

check_strength()

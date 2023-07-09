
password = input('Enter password: ')
#password = '1234'
print('Password: ', password)

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

character_type = check_character_type()
print(character_type)

def check_password_length():
    password_length = len(password)
    return password_length

password_length = check_password_length()
print(password_length)

U = 'U'
L = 'L'
N = 'N'
S = 'S'


def check_strength():

    # Only numbers in password
    if N in character_type and U not in character_type and L not in character_type and S not in character_type:
        print('Password consits only of numbers')

        if password_length <= 15:
            print('Your password is to weak and failed.')
        elif password_length == 16:
            print('Password is weak')
        elif password_length >= 17 and password_length <= 18:
            print('Password is intermediate.')
        else:
            print('Password is strong')

    # Only upper case letters in password
    if N not in character_type and U in character_type and L not in character_type and S not in character_type:
        print('Password consist only of upper case letters')

        if password_length <= 10:
            print('Your password is to weak and failed.')
        elif password_length == 11:
            print('Password is weak')
        elif password_length == 12:
            print('Password is intermediate.')
        else:
            print('Password is strong')

    # Only lower case letters in password
    if N not in character_type and U not in character_type and L in character_type and S not in character_type:
        print('Password consist only of lower case letters')

        if password_length <= 10:
            print('Your password is to weak and failed.')
        elif password_length == 11:
            print('Password is weak')
        elif password_length == 12:
            print('Password is intermediate.')
        else:
            print('Password is strong')

    # Upper and lower case letters in password
    if N not in character_type and U in character_type and L in character_type and S not in character_type:
        print('Password consist of upper and lower case letters')

        if password_length <= 9:
            print('Your password is to weak and failed.')
        else:
            print('Password is strong')

    # Upper case letters and numbers in password
    if N in character_type and U in character_type and L not in character_type and S not in character_type:
        print('Password consist of upper case letters and numbers')

        if password_length <= 9:
            print('Your password is to weak and failed.')
        else:
            print('Password is strong')


    # Lower case letters in password
    if N in character_type and U not in character_type and L in character_type and S not in character_type:
        print('Password consist of lower case letters and numbers')

        if password_length <= 9:
            print('Your password is to weak and failed.')
        else:
            print('Password is strong')

    # Numbers, Upper and lower case letters in password
    if N in character_type and U in character_type and L in character_type and S not in character_type:
        print('Password consist of numbers, upper and lower case letters')

        if password_length <= 8:
            print('Your password is to weak and failed.')
        elif password_length ==9:
            print('Your password is weak')
        elif password_length == 10:
            print('Your password is intermediate.')
        else:
            print('Password is strong')

    # Numbers, Upper and lower case letters and special characters in password
    if N in character_type and U in character_type and L in character_type and S in character_type:
        print('Password consist of numbers, upper and lower case letters and special characters')

        if password_length <= 8:
            print('Your password is to weak and failed.')
        elif password_length ==9:
            print('Your password is intermediate')
        else:
            print('Password is strong')
    return

check_strength()

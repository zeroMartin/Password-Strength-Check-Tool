
#password = input('Enter password: ')
password = 'Ma5%'
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

if N in character_type and password_length <= 15:
    print('Your password is too weak!')
elif N in character_type and password_length <= 18:
    print('Your password strenght is good!')
elif n in character_type and password_length > 18:
    print('Your password has medium strenght!')
else:
    ('Break')

#if U in character_type and L in character_type:
#    print('We have upper and lower case letters')
#else:
#    print('No upper case')



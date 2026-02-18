# Skills Test 3rd Quarter
from pyscript import display, document


def username_verification(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    username_length = len(username)

    if username_length == 0:
        document.getElementById('output').innerHTML = \
            f'Please input a username to proceed.'
    elif username_length < 7:
        display(f'Your username is too short. Add at least {7 - username_length} more character/s to proceed.', target='output')
    else:
        return(True)


def password_verification(e):
    document.getElementById('output').innerHTML = ''

    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)

    if password_length == 0:
        document.getElementById('output').innerHTML = \
            f'Please input a password to proceed.'
    elif password_length < 9:
        document.getElementById('output').innerHTML = \
            f'Your password is too short. Add at least {9 - password_length} more character/s to proceed.'
    elif not password_has_letter:
        document.getElementById('output').innerHTML = \
            'Password must contain at least one letter.'
    elif not password_has_number:
        document.getElementById('output').innerHTML = \
            'Password must contain at least one number.'
    else:
        document.getElementById('output').innerHTML = 'Password is valid!'
        return (True)


def account_creation(e):
    document.getElementById('output').innerHTML = ' '

    if username_verification(e) == True and password_verification(e) == True:
        display(f'Account created. You may now log in using your credentials.', target='output')
    else:
        display(f'Try again', target='output')
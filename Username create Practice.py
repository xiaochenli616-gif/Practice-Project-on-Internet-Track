
username = input('Please enter your username:')
username.find(' ')

if len(username) > 12:
    print('Username can not exceed 12 characters')
elif not username.find(' ') == -1:
    print('Username can not contain spaces')
elif not username.isalpha():
    print('Username must be numbers')
else:
    print(f'Welcome to this space!, {username}')
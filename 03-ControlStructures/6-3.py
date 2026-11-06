new_password = input('Enter new password: ')
print('Password too short (min. 12 chars)' if len(new_password) < 12 else 'Password is valid')

login = 'jakub'
password = '1234'
entered_login = input('Login: ')
entered_password = input('Password: ')
print('You are logged in' if login == entered_login and password == entered_password
      else 'Incorrect login or password!!')

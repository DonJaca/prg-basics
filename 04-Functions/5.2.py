import keyboard

first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter surname: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')

print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary:', salary)

number1 = float(input('First number: '))
operator = input('Operation (+, -, *, /): ')
number2 = float(input('Second number: '))
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    raise ValueError('Unsupported operator')
print(f'{number1} {operator} {number2} = {result}')

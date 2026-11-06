def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '%':
        return number1 % number2
    if operator == '**':
        return number1 ** number2
    raise ValueError('Unknown operator')


print(f(2, 3, '+'))
print(f(2, 3, '%'))
print(f(2, 3, '**'))
print(f(2, 3, '*'))
print(f(2, 3, '-'))

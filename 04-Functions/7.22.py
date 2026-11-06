def f(expression):
    result = int(expression[0])
    index = 1
    while index < len(expression):
        number = int(expression[index + 1])
        result = result + number if expression[index] == '+' else result - number
        index += 2
    return result


print(f('2+3'))
print(f('3+8+1'))
print(f('2+3-4+5-0'))

def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


jakub = int(input('Enter integer number: '))
print(f'The sum of the digits in the number {jakub} is {sum_digits(jakub)}')

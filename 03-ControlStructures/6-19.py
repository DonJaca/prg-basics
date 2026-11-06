number = int(input('Enter decimal number: '))
if number < 0:
    raise ValueError('Number must be non-negative')
original = number
bits = '0' if number == 0 else ''
while number:
    bits = str(number % 2) + bits
    number //= 2
print(f'{original}(10) = {bits}(2)')

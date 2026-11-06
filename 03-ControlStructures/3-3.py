x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(f'At least one of the numbers {x} and {y} is not negative' if x >= 0 or y >= 0
      else 'Both numbers are negative')

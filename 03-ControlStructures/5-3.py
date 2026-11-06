total = count = 0
while True:
    number = int(input('Enter a number (0 to stop): '))
    if number == 0:
        break
    total += number
    count += 1
print(f'The total sum of the numbers is: {total}')
print(f'The arithmetic mean is: {total / count if count else 0}')

total = 0
for number in range(1, 11):
    if number % 2 != 0:
        continue
    total += number
print(f'Sum of even numbers in the range <1,10> is {total}')

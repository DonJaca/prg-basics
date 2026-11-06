n = int(input('Enter N: '))
i = total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print(f'The sum of even numbers from 1 to {n} is: {total}')

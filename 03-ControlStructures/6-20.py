amount = int(input('Enter the amount in PLN: '))
if amount < 0:
    raise ValueError('Amount must be non-negative')
print(f'5 PLN coins: {amount // 5}')
amount %= 5
print(f'2 PLN coins: {amount // 2}')
print(f'1 PLN coins: {amount % 2}')

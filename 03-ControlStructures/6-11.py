products = int(input('Number of products purchased: '))
price = float(input('Product price: '))
total = price * (products if products <= 2 else 2 + (products - 2) * .75)
print(f'Amount to pay: {total:.2f}')

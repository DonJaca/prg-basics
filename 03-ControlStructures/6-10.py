current = float(input('Current product price: '))
previous = float(input('Previous product price: '))
reduction = (previous - current) / previous * 100
if reduction >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {reduction:.0f}%')

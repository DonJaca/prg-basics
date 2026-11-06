size = input('Enter size symbol: ')
sizes = {'S': 'Small size', 'M': 'Medium size', 'L': 'Large size', 'XL': 'Extra large size'}
print(sizes.get(size, 'Incorrect symbol'))

mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))
rates = {'A': 7, 'M': 9, 'E': 6}
if mode not in rates:
    raise ValueError('Invalid driving mode')
print(f'Total fuel consumption: {distance * rates[mode] / 100:g} liters')

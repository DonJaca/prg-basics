product = input('Select washing program (jacket/underwear/shoes): ')
rinse = input('Extra rinse? (y/n): ').lower() == 'y'
spin = input('Extra spin? (y/n): ').lower() == 'y'
times = {'jacket': 40, 'underwear': 70, 'shoes': 20}
if product not in times:
    raise ValueError('Unknown program')
print(f'Total washing time: {times[product] + (15 if rinse else 0) + (9 if spin else 0)} minutes')

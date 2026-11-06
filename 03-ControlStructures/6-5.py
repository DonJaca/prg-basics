hours = int(input('Hours parked: '))
fee = 0 if hours < 1 else 5 if hours <= 2 else 15 if hours <= 6 else 20
print(f'Parking fee: {fee} PLN')

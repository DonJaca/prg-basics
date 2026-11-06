month = int(input('Enter month number (1..12): '))
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if month not in days:
    raise ValueError('Month must be from 1 to 12')
print(f'Month {month} has {days[month]} days')

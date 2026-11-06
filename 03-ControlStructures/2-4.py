month = int(input('Enter month number (1..12): '))
if not 1 <= month <= 12:
    raise ValueError('Month must be from 1 to 12')
quarter = (month - 1) // 3 + 1
print(f'Month {month} is in quarter {quarter}')

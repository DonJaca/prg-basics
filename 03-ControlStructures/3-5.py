month = int(input('Enter month number (1..12): '))
day = int(input('Enter day number: '))
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
valid = month in days and 1 <= day <= days[month]
print(f'Day {day} for month {month} is {"correct" if valid else "incorrect"}')

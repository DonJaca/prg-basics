time24 = input('Enter time (24-hour format): ')
hour, minute = (int(part) for part in time24.split(':'))
if not 0 <= hour <= 23 or not 0 <= minute <= 59:
    raise ValueError('Invalid time')
print(f'Time in 12-hour format: {hour % 12 or 12}:{minute:02d}{"am" if hour < 12 else "pm"}')

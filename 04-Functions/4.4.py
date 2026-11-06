def day_name(day_number):
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    if 1 <= day_number <= 7:
        return days[day_number - 1]
    return ''


print(day_name(5))
print(day_name(3))
print(day_name(7))

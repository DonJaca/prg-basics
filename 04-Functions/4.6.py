def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'
    if hours == 0:
        return f'12:{minutes:02d}am'
    if hours < 12:
        return f'{hours}:{minutes:02d}am'
    if hours == 12:
        return f'12:{minutes:02d}pm'
    return f'{hours - 12}:{minutes:02d}pm'


tests = ((15, 38, '24'), (8, 3, '24'), (0, 5, '24'), (11, 15, '12'),
         (0, 7, '12'), (7, 30, '12'), (12, 46, '12'), (13, 10, '12'),
         (19, 2, '12'))
for test in tests:
    print(time_string(*test))

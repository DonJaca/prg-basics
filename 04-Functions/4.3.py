def pts_to_grade(points):
    if points >= 18:
        return 'Excellent'
    if points >= 14:
        return 'Good'
    if points >= 10:
        return 'Satisfactory'
    return 'Fail'


jakub = 15
print(f'You scored {jakub} points on the test. Your final grade is {pts_to_grade(jakub)}')

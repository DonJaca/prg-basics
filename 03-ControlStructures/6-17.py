x = int(input('x = '))
y = int(input('y = '))
if x == 0 and y == 0:
    location = 'the origin'
elif x == 0:
    location = 'the y-axis'
elif y == 0:
    location = 'the x-axis'
else:
    location = ('the first' if x > 0 and y > 0 else 'the second' if y > 0
                else 'the third' if x < 0 else 'the fourth') + ' quadrant'
print(f'Point P({x},{y}) is in {location} of the coordinate system')

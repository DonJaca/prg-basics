import math


def triangle_area(a, b, c):
    semiperimeter = (a + b + c) / 2
    return math.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))


for sides in ((3, 4, 5), (5, 12, 13), (7, 24, 25)):
    print(f'The area of a triangle with sides {sides} is {triangle_area(*sides)}')

jakub = tuple(map(float, input('Enter three side lengths: ').split()))
print(triangle_area(*jakub))

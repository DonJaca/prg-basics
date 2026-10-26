import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    pole = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return pole

print(triangle_area(3,4,5))

def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    return sum(int(digit) for digit in product_code[:3]) % 7 == int(product_code[3])


print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))

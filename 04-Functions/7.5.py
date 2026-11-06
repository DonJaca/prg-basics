def f(binary_number):
    return bool(binary_number) and all(digit in '01' for digit in binary_number)


print(f('101101'))
print(f('1311a10100'))

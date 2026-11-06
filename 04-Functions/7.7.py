def f(number, even):
    digits = (int(digit) for digit in str(abs(number)))
    return sum(digit for digit in digits if digit % 2 == 0) if even else sum(
        digit for digit in digits if digit % 2 != 0)


print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))

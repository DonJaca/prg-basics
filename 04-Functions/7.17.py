def f(number):
    digits = str(abs(number))
    return sum(int(digit) for digit in digits if digits.count(digit) > 1)


print(f(1027))
print(f(230335))
print(f(513553007))

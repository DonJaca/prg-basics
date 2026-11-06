def f(number1, number2, number3):
    numbers = (number1, number2, number3)
    return max(numbers) - min(numbers)


print(f(7, 4, 9))
print(f(2, 12, 8))

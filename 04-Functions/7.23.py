def f(x, y):
    return sum(number for number in range(x, y + 1)
               if number % 2 == 0 and number % 3 == 0 and number % 4 != 0)


print(f(1, 20))
print(f(10, 30))

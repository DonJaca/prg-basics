def f(n):
    found = 0
    number = 1
    while found < n:
        number += 1
        if all(number % divisor for divisor in range(2, int(number ** 0.5) + 1)):
            found += 1
    return number


print(f(1))
print(f(5))

def f(n):
    first, second = 0, 1
    for _ in range(n - 1):
        first, second = second, first + second
    return first


print(f(5))
print(f(9))

first, second = 0, 1
for _ in range(20):
    print(first, end=' ')
    first, second = second, first + second
print()

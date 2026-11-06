def f(palindrome):
    text = ''.join(palindrome.lower().split())
    return text == text[::-1]


print(f('radar'))
print(f('12-11-21'))
print(f('book'))

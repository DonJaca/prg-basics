def f(password):
    return len(password) >= 6 and len(password) == len(set(password))


print(f('ax15'))
print(f('book123'))
print(f('A2water3'))
print(f('qwerty'))
print(f(''))

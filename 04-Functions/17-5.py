def f(a):
    splitted = "".join(a.lower().split())
    return splitted == splitted[::-1]

print(f("radar") )
print(f("12-11-21") )
print(f("book"))
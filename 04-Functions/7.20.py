def f(name):
    return ''.join(word[0] for word in name.split())


print(f('Internet of Things'))
print(f('For Your Information'))
print(f('Python'))

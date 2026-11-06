age = int(input('Enter age: '))
group = 'Child' if age < 13 else 'Teen' if age <= 19 else 'Adult' if age <= 64 else 'Senior'
print(group)

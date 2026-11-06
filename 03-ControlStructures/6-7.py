name1 = input('First person name: ')
age1 = int(input('First person age: '))
name2 = input('Second person name: ')
age2 = int(input('Second person age: '))
print(f'Both {name1} and {name2} are adults' if age1 >= 18 and age2 >= 18
      else f'Either {name1} or {name2} is not an adult')

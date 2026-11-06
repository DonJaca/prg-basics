age = float(input("Enter the dog's age in human years: "))
dog_age = age * 10.5 if age <= 2 else 21 + (age - 2) * 4
print(f"The dog's age in dog's years is {dog_age:g} years.")

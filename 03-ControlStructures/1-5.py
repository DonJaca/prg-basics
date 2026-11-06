basic_salary = 5000
bonus = float(input('Bonus percent (0 for no bonus): '))
total_salary = basic_salary * (1 + bonus / 100)
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {"Yes" if bonus else "No"}')
print(f'Total salary: {total_salary}')

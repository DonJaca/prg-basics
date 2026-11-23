categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
for n in range(len(categories)-1):
    max_expensen_cat = ""
    max_expensen_exp = 0
    if expenses[n]>expenses[n+1]:
        max_expensen_cat = categories[n]
        max_expensen_exp = expenses[n]
    else:
        max_expensen_cat = categories[n+1]
        max_expensen_exp = expenses[n+1]

print(max_expensen_cat,max_expensen_exp)
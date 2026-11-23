# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]
food = 0
trans = 0
utili = 0
# Calculates expenses
# Use loop statements
for j in range(len(monthly_expenses)-1):
    food += monthly_expenses[j][0]
    trans += monthly_expenses[j][1]
    utili += monthly_expenses[j][2]
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',trans)
print('Utilities:',utili)
print('Week 1:',...)
print('Week 2:',...)
print('Week 3:',...)
print('Week 4:',...)
print('---------------')
print('TOTAL:',food+trans+utili)
###
# The weather station report
#
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# number of mesaurements
mesaurements = len(temperatures)
print(mesaurements)
print(sum(temperatures)/len(temperatures))
print(max(temperatures))
print (min(temperatures))
below_zero = 0
for temp in temperatures:
    if temp <0:
        below_zero +=1
print(below_zero)



car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

def bubbleSort(tabble):
    for n in range(len(tabble)-1):
        if n+1 > n:
            tabble[n+1],tabble[n]=tabble[n],tabble[n+1]
        else:
            continue
    return(tabble)

print(bubbleSort(car_fuel_consumption))
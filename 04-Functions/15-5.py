def f(d):
    osoby = d
    suma = 0
    print(d)
    for person in osoby:
        if person == "+":
            suma +=1
        elif person =="-":
            suma -=1
        if suma==3:
            return True
            break
    else:
        return False

print(f("+-+++-+---"))

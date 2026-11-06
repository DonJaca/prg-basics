count = int(input('How many prime numbers? '))
found = []
candidate = 2
while len(found) < count:
    divisor = 2
    prime = True
    while divisor * divisor <= candidate:
        if candidate % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        found.append(candidate)
    candidate += 1
print('Prime numbers:', *found)

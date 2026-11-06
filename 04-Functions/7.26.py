def f(dice):
    best_number = ''
    best_length = 0
    current_number = ''
    current_length = 0
    for number in dice:
        if number == current_number:
            current_length += 1
        else:
            current_number = number
            current_length = 1
        if current_length > best_length:
            best_number = current_number
            best_length = current_length
    return int(best_number)


print(f('5233165554211'))
print(f('2133'))

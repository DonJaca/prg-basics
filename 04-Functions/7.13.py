def f(detector):
    people = 0
    most_people = 0
    for sign in detector:
        people += 1 if sign == '+' else -1
        most_people = max(most_people, people)
    return most_people >= 3


print(f('+-+++-+---'))
print(f('+-+-+-+-'))
print(f('+-++-+--'))
print(f('+-++-++-+---'))

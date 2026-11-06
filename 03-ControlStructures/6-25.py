correct_pin = '0805'
for attempt in range(3):
    if input('Enter the PIN code: ') == correct_pin:
        print('Correct PIN')
        break
    print('Incorrect PIN')
else:
    print('Sorry, your payment card has been blocked.')

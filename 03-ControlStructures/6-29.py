for row in range(1, 8):
    print(*(row + 7 * column for column in range(7)))

for number in range(1, 31):
    print('BINGO' if number % 15 == 0 else 'THREE' if number % 3 == 0
          else 'FIVE' if number % 5 == 0 else number, end=' ')
print()

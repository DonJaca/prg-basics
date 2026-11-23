# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

for row in tic_tac_toe_board:
    for i in range(len(tic_tac_toe_board)):
        print(tic_tac_toe_board[0][i])
        print(tic_tac_toe_board[1][i])
        print(tic_tac_toe_board[2][i])
    print()
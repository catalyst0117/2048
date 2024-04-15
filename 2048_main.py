from utilities import generate_piece, print_board

DEV_MODE = True


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    continue_input = True
    for row in game_board:
        for piece in row:
            if piece == 0:
                continue_input = False
    for row in game_board:
        for i in range(0, 3):
            if row[i] == row[i + 1]:
                continue_input = False
    for row in range(0, 4):
        for i in range(0, 3):
            if game_board[i][row] == game_board[i + 1][row]:
                continue_input = False
    return continue_input


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    def apply_piece(game_board):
        initial = generate_piece(game_board)
        game_board[initial['row']][initial['column']] = initial['value']

    def process(game_board):
        for row_num, row in enumerate(game_board):
            list_new = []
            for piece in row:
                if piece != 0:
                    list_new.append(piece)
            i = 0
            while i < (len(list_new) - 1):
                if list_new[i] == list_new[i + 1]:
                    list_new[i] *= 2
                    del list_new[i + 1]
                i += 1
            n = len(list_new)
            for zero in range(4 - n):
                list_new.append(0)
            game_board[row_num] = list_new
    apply_piece(game_board)
    while True:
        apply_piece(game_board)
        loss = game_over(game_board)
        print_board(game_board)
        if loss:
            print('lost')
            break
        user_input = input()
        while user_input not in ['q', 'w', 'a', 's', 'd']:
            user_input = input()
        if user_input == 'q':
            print('Goodbye')
            break
        elif user_input == 'a':
            process(game_board)
        elif user_input == 'd':
            for i in range(0, 4):
                game_board[i].reverse()
            process(game_board)
            for i in range(0, 4):
                game_board[i].reverse()
        elif user_input == 'w':
            for m in range(0, 4):
                for n in range(0, m):
                    switch_transition = game_board[m][n]
                    game_board[m][n] = game_board[n][m]
                    game_board[n][m] = switch_transition
            process(game_board)
            for m in range(0, 4):
                for n in range(0, m):
                    switch_transition = game_board[m][n]
                    game_board[m][n] = game_board[n][m]
                    game_board[n][m] = switch_transition
        elif user_input == 's':
            for m in range(3, -1, -1):
                for n in range(m, -1, -1):
                    switch_transition = game_board[m][n]
                    game_board[m][n] = game_board[n][m]
                    game_board[n][m] = switch_transition
            for i in range(0, 4):
                game_board[i].reverse()
            process(game_board)
            for i in range(0, 4):
                game_board[i].reverse()
            for m in range(3, -1, -1):
                for n in range(m, -1, -1):
                    switch_transition = game_board[m][n]
                    game_board[m][n] = game_board[n][m]
                    game_board[n][m] = switch_transition
        checker = True
        for row in game_board:
            if 2048 in row:
                checker = False
        if not checker:
            break
    return game_board


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])

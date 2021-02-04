'''
This module sets whether the playing field of the logic puzzle is ready to start the game
'''


def horizontal_check(board):
    '''
    Checks whether there are no repetitions of numbers in the rows of the table

    >>> horizontal_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> horizontal_check(["**** ****", "***11****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> horizontal_check(["987654321", "123456789", "**  3****", "123456789", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''

    for i in range(9):
        for j in range(9):
            for m in range(9):
                if board[i][j] == board[i][m] and j != m and board[i][j] != '*' and board[i][j] != ' ':
                    return False
    return True
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


def vertical_check(board):
    '''
    Checks whether there are no repetitions of numbers in the columns of the table

    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "  2  ****", "  8  2***", "  2  ****"])
    False
    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3      **", "  8  2***", "  2  ****"])
    True
    '''

    for i in range(9):
        for j in range(9):
            for m in range(9):
                if board[j][i] == board[m][i] and j != m and board[j][i] != '*' and board[j][i] != ' ':
                    return False
    return True


def all_in_row(board):
    '''
    Creates a dictionary in which writes values ​​from corner to line

    >>> all_in_row(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    {0: '****  3    2  ****', 1: '***  6   8  2***', 2: '** 4     1  **', 3: '*1     83  *', 4: '  31  9 5 '}
    >>> all_in_row(["987654321", "123456789", "**  3****", "123456789", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    {0: '91*1  3    2  ****', 1: '82*2 6   8  2***', 2: '73 3     1  **', 3: '64 4   83  *', 4: '5535  9 5 '}
    '''

    res = {}
    k = 0
    for i in range(5):
        summa = ''
        for j in range(9 - k):
            summa += board[j][i]
        res[i] = summa
        k += 1

    k = 0
    helping_counter = 0
    for i in range(8,3,-1):
        res[i - 8 + k + helping_counter] += board[i][k:]
        k += 1
        helping_counter += 1

    return res


def corner_check(board):
    '''
    Checks whether there are no repetitions of numbers in the corners of the table

    >>> corner_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> corner_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "2 8  2***", "  2  ****"])
    False
    '''

    rows = all_in_row(board)
    for i in range(5):
        rows[i] = rows[i].replace('*', '')
        for m in range(9):
            for n in range(9):
                if rows[i][m] == rows[i][n] and m != n and rows[i][m] != ' ':
                    return False
    return True
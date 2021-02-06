'''
https://github.com/firstgenius/Puzzles.git
This module sets whether the playing field of the logic puzzle is ready to start the game
'''


def horizontal_check(board):
    '''
    Checks whether there are no repetitions of numbers in the rows of the table

    >>> horizontal_check(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> horizontal_check(["**** ****", "***11****", "**  3****", "* 4 1****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> horizontal_check(["987654321", "123456789", "**  3****", "123456789",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''

    for i in range(9):
        for j in range(9):
            for ele in range(9):
                if board[i][j]==board[i][ele] and j!=ele and board[i][j]!='*' and board[i][j]!=' ':
                    return False
    return True


def all_in_row(board):
    '''
    Creates a dictionary in which writes values from corner to line

    >>> all_in_row(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *",\
        "3   1  **", "  8  2***", "  2  ****"])
    {0: '****  3    2  ****', 1: '***  6   8  2***', 2: '** 4     1  **', 3: '*1     83  *',\
 4: '  31  9 5 '}
    >>> all_in_row(["987654321", "123456789", "**  3****", "123456789", "     9 5 ", " 6  83  *",\
        "3   1  **", "  8  2***", "  2  ****"])
    {0: '91*1  3    2  ****', 1: '82*2 6   8  2***', 2: '73 3     1  **', 3: '64 4   83  *',\
 4: '5535  9 5 '}
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


def vertical_check(board):
    '''
    Checks whether there are no repetitions of numbers in the columns of the table

    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
        " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
        " 6  83  *", "  2  ****", "  8  2***", "  2  ****"])
    False
    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
        " 6  83  *", "3      **", "  8  2***", "  2  ****"])
    True
    '''

    for i in range(9):
        for j in range(9):
            for ele in range(9):
                if board[j][i]==board[ele][i] and j!=ele and board[j][i]!='*' and board[j][i]!=' ':
                    return False
    return True


def corner_check(board):
    '''
    Checks whether there are no repetitions of numbers in the corners of the table

    >>> corner_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *",\
        "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> corner_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *",\
        "3   1  **", "2 8  2***", "  2  ****"])
    False
    '''

    rows = all_in_row(board)
    for i in range(5):
        rows[i] = rows[i].replace('*', '')
        for elem in range(9):
            for j in range(9):
                if rows[i][elem] == rows[i][j] and elem != j and rows[i][elem] != ' ':
                    return False
    return True


def validate_board(board):
    '''
    Checks whether the playing field of the logic puzzle is ready to start the game

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
        " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
        " 6  83  *", "3      **", "  8  2***", "  2  ****"])
    True
    '''

    return horizontal_check(board) and vertical_check(board) and corner_check(board)

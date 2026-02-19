def isValidSudoku(board):
    # rows
    # row_hash_set = set()
    # row_list = []
    # for row in board:
    #     for col in row:
    #         curr = col
    #         if curr != ".":
    #             row_hash_set.add(int(curr))
    #             row_list.append(int(curr))
    #     print(row_hash_set)
    #     print(sorted(row_list))
    #     if (row_hash_set != row_list):
    #         return False
    # columns
    col_hash_set = set()
    col_list = []
    row = 0
    col = 0
    while col < len(board):
        curr = board[row][col]
        if row == 8:
            row = 0
            col +=1
        else:
            if curr != ".":
                col_hash_set.add(int(curr))
                col_list.append(int(curr))
            row +=1
        print(col_hash_set)
        print(sorted(col_list))

    # 3x3

    return True

board=[[".",".","4",".",".",".","6","3","."],
       [".",".",".",".",".",".",".",".","."],
       ["5",".",".",".",".",".",".","9","."],
       [".",".",".","5","6",".",".",".","."],
       ["4",".","3",".",".",".",".",".","1"],
       [".",".",".","7",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board))


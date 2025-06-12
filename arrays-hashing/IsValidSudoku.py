def isValidSudoku(board):
    for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
    for col in range(9):
        seen = set()
        for i in range(9):
            if board[i][col] == ".":
                continue
            if board[i][col] in seen:
                return False
            seen.add(board[i][col])
        
    for square in range(9):
        seen = set()
        for i in range(3):
            for j in range(3):
                row = (square//3) * 3 + i
                col = (square % 3) * 3 + j
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
    return True

board=[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board))


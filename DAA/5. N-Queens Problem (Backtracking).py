# 5. N-Queens Problem

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i][col] == "Q":
            return False
    # check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    # check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            solve_n_queens(board, row + 1, n)
            board[row][col] = "."

n = 4
board = [["."] * n for _ in range(n)]
board[0][1] = "Q"  # first queen placed
print("Initial Board:")
print_board(board)
print("Solutions:")
solve_n_queens(board, 1, n)

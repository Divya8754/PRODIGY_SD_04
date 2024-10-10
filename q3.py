def print_board(board):
    """Helper function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty(board):
    """Find an empty space in the Sudoku board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 represents an empty cell
                return i, j  # row, col
    return None

def is_valid(board, num, row, col):
    """Check if a number can be placed in the given position."""
    # Check the row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solve the Sudoku board using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Solved

    row, col = empty

    for num in range(1, 10):  # Numbers 1 to 9
        if is_valid(board, num, row, col):
            board[row][col] = num  # Place the number

            if solve_sudoku(board):  # Recursively solve
                return True

            board[row][col] = 0  # Reset if not valid

    return False  # Trigger backtracking

# Example input Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
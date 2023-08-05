def is_safe(board, row, col, num):
    # Check if 'num' is not present in current row, column, and box
    return (
        not any(num == board[row][i] for i in range(9)) and
        not any(num == board[i][col] for i in range(9)) and
        not any(num == board[row//3*3 + i//3][col//3*3 + i%3] for i in range(9))
    )

def find_empty_cell(board):
    # Find the first empty cell (cell with value 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # All cells are filled, the puzzle is solved

    row, col = empty_cell
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack and try the next number
    return False

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
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

    if solve_sudoku(puzzle):
        for row in puzzle:
            print(row)
    else:
        print("No solution exists for the given Sudoku puzzle.")

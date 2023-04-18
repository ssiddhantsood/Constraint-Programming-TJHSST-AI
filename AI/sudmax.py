# Initialize the puzzle grid with zeros
grid = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Function to check if a number is valid in a given position
def is_valid(grid, row, col, num):
  # Check if the number is already in the row
  for i in range(9):
    if grid[row][i] == num:
      return False

  # Check if the number is already in the column
  for i in range(9):
    if grid[i][col] == num:
      return False

  # Check if the number is already in the 3x3 block
  block_row = row // 3
  block_col = col // 3
  for i in range(block_row * 3, block_row * 3 + 3):
    for j in range(block_col * 3, block_col * 3 + 3):
      if grid[i][j] == num:
        return False

  # If the number is not in the row, column, or block, it is valid
  return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        # Try each number from 1 to 9
        for num in range(1, 10):
          if is_valid(grid, row, col, num):
            # If the number is valid, place it in the grid
            grid[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(grid):
              return True

            # If the puzzle cannot be solved with this number,
            # backtrack and try the next number
            grid[row][col] = 0

        # If no number works, return False to indicate that the puzzle
        # cannot be solved with the given numbers
        return False

  # If the grid is full, return True to indicate that the puzzle is solved
  return True

# Solve the puzzle
solve_sudoku(grid)

print(grid)
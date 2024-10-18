# Function to print the N-Queen board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

# Function to check if placing a queen at board[row][col] is safe
def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

# Backtracking function to solve the N-Queens problem
def solve_nqueens(board, col, n):
    # If all queens are placed
    if col >= n:
        return True

    # Try placing the queen in each row of this column
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen
            board[i][col] = 'Q'

            # Recur to place the rest of the queens
            if solve_nqueens(board, col + 1, n):
                return True

            # If placing queen here doesn't lead to a solution, remove it (backtrack)
            board[i][col] = '.'

    # If the queen cannot be placed in any row in this column, return False
    return False

# Function to solve the N-Queens problem and generate the matrix
def nqueens(n):
    # Initialize the board
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Manually place the first queen (let's say at position [0, 0])
    board[0][0] = 'Q'

    # Solve the problem for the remaining queens starting from column 1
    if not solve_nqueens(board, 1, n):
        print("Solution does not exist")
        return False

    # Print the final board
    print_board(board)
    return True

# Set the size of the chessboard (for example, 8 for an 8x8 board)
n = 8
nqueens(n)


'''
  Q . . . . . . .
. . . . . . Q .
. . . . Q . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . .
'''

'''
   Same major diagonal: i - j == k - l
Same minor diagonal: i + j == k + l
Let's verify:

Row	Column	Major Diagonal (i - j)	Minor Diagonal (i + j)
0	0	0	0
1	6	-5	7
2	4	-2	6
3	7	-4	10
4	1	3	5
5	3	2	8
6	5	1	11
7	2	5	9
For major diagonals (i - j): No two queens share the same major diagonal value, which is correct.
For minor diagonals (i + j): No two queens share the same minor diagonal value, which is also correct. '''

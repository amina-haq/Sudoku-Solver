
# very basic sudoku board
# to understand back tracking
def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False
    
    for x in range(9):
        if grid [x][col] == number:
            return False
        
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
            
    return True

def solve(grid, row, col):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    for num in range(1, 10):

        if is_valid_move(grid, row, col, num):

            grid[row][col] = num

            if solve(grid, row, col +1):
                return True
            
        grid[row][col] = 0
    return False

grid = [[4,0,0,0,0,0,8,0,5],
        [0,3,0,0,0,0,0,0,0],
        [0,0,0,7,0,0,0,0,0],
        [0,2,0,0,0,0,0,6,0],
        [0,0,0,0,8,0,4,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,6,0,3,0,7,0],
        [5,0,0,2,0,0,0,0,0],
        [1,0,4,0,0,0,0,0,0]]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

else:
    print("No Solution For This Sudoku")
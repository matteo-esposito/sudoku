"""
Author: Matteo Esposito
Date: Dec 14, 2019
"""

def solve(board):
    """Aggregator function that does the solving."""
    position = [0,0]
    
    if not find_empty_location(board, position):
        return True # Done.
    
    e_row = position[0]
    e_col = position[1]
    
    for potential_solution in range(1, 10):
        if safe(board, e_row, e_col, potential_solution):
            board[e_row][e_col] = potential_solution
            
            if solve(board):
                return True #Done.
            
            # Backtracking! If we made a mistake, restore to 0 and rerun.
            board[e_row][e_col] = 0
    
    return False

def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False    
    
def in_row(board, row, entry):
    for i in range(9):
        if (board[row][i] == entry):
            return True
    return False
    
def in_col(board, col, entry):
    for i in range(9):
        if (board[i][col] == entry):
            return True
    return False
    
def in_subgrid(board, row, col, entry):
    for i in range(3):
        for j in range(3):
            if (board[row+i][col+j] == entry):
                return True
    return False
    
def safe(board, row, col, entry):
    """Check if entry is legit."""
    
    # Mod the in_subgrid arguments to be able to search the grid from (0,0) to (2,2),
    # regardless of if the current row or col is the first row or col of the subgrid.
    return not in_row(board, row, entry) and not in_col(board, col, entry) and not in_subgrid(board, row-row%3, col-col%3, entry)

def printf(board):
    """Print solved grid nicely."""
    for i in range(9): 
        for j in range(9): 
            print(board[i][j], end = ",") 
        print('\n') 

if __name__ == '__main__':

    # 0 corresponds to empty cell
    # 9x9 grid with 3x3 subgrids.
    grid = [[3,0,6,5,0,8,4,0,0], 
             [5,2,0,0,0,0,0,0,0], 
             [0,8,7,0,0,0,0,3,1], 
             [0,0,3,0,1,0,0,8,0], 
             [9,0,0,8,6,3,0,0,5], 
             [0,5,0,0,9,0,6,0,0], 
             [1,3,0,0,0,0,2,5,0], 
             [0,0,0,0,0,0,0,7,4], 
             [0,0,5,2,0,6,3,0,0]] 

    if solve(grid):
        printf(grid)
    else:
        print("No solution.")
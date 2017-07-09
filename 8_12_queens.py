# Write an algorithm to print all ways of arranging eight queens on 8*8 chess board, so that none of them share the same column, row and diagonal.
# In this case, "diagonal" means all diagonal, not just the two that bisect the board.
import copy
def queens(n):
    res = []
    columns = [-1]*8
    placeQueens(columns, 0, res)
    return res

def placeQueens(columns, row, res):
    if row == len(columns): 
        res.add(copy.copy(columns))
    else:
        for col in range(len(columns)):
            if checkValid(columns, row, col):
                columns[row] = col
                placeQueens(columns, row+1, res)

def checkValid(columns, row, col):
    for r in range(row):
        c = columns[r]
        if col == c:
            return False
        
        colDistance = abs(col-c)
        rowDistance = row - r
        if colDistance == rowDistance:
            return False

    return True
    
    

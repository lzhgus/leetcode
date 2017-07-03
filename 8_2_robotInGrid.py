# Robot in a Grid 
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can ony move in two directions, right and down, but certain cells are "off limits" 
# such that the robot cannot step on them. Design an algorigthm to find a path for the robot from the to left to the bottom right

# the only way to move to spot(r,c) is by moving to one of the adjacent spots(r-1,c) or (r, c-1)

def getPath(maze):
    if not maze or len(maze) == 0: return None
    path = []
    if getPathHelper(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def getPathHelper(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]: 
        return False

    isAtOrigin = True if (row==0 and col==0) else False

    if isAtOrigin or getPathHelper(maze, row-1, col, path) or getPathHelper(maze, row, col-1, path):
        path.append((row,col))
        return True
    return False


# avoid duplicate works

def getPath(maze):
    if not maze or len(maze)==0: return None
    path = []
    failedPoint = []
    if helper(maze, len(maze)-1, len(maze[0])-1, path, failedPoint):
        return Path
    return None

def helper(maze, row, col, path, failedPoint):
    if row < 0 or col < 0 or not maze[row][col]:
        return False

    p = (row, col)
    if p in failedPoint:
        return False
    
    isAtOrigin = True if row==0 and col==0 else False
    
    if isAtOrigin or helper(maze, row-1, col, path, failedPoint) or helper(maze, row, col-1, path, failedPint):
        path.append(p)
        return True

    failedPoint.append(p)
    return False 
        

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def setLeft(self, left):
        leftNode = TreeNode(left)
        self.left = leftNode

    def setRight(self, right):
        rightNode = TreeNode(right)
        self.right = rightNode

def countPathsWithSum(root, target):
    if not root: return 0
    
    pathFromRoot = countPathsFromRoot(root, target, 0)

    pathOfLeft = countPathsWithSum(root.left, target)
    pathOfRight = countPathsWithSum(root.right, target)

    return pathFromRoot + pathOfLeft + pathOfRight

def countPathsFromRoot(node, target, curSum, total = 0):
    if not node: return 0
    curSum += node.val

    if curSum == target:
        total+=1

    countPathsFromRoot(node.left, target, curSum, total)
    countPathsFromRoot(node.right, target, curSum, total)

    return total

def findSum(node, givenSum, path=None, depth=0):
    if not node: return
    if not path: path = []
    if len(path) > depth:
        path[depth] = node.val
    else:
        path.append(node.val)

    tmp = 0
    for i in range(depth, -1, -1):
        tmp += path[i]
        if tmp == givenSum:
            printPath(path,i,depth)
        
    findSum(node.left, givenSum, path, depth+1)
    findSum(node.right, givenSum, path, depth+1)

def printPath(path, start, end):
    for i in range(start, end + 1):
        print path[i],
    print ""

def main():
    givenSum = 7
    root = TreeNode(1)
    root.setLeft(2)
    root.setRight(3)
    root.left.setLeft(4)
    root.left.setRight(5)
    root.right.setLeft(3)
    root.right.setRight(4)
    root.left.right.setLeft(7)

    res = countPathsWithSum(root, givenSum)
    findSum(root, givenSum)

if __name__ == "__main__":
    main()

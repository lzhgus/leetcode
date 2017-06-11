class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def setLeft(self, leftValue):
        leftNode = BinaryTreeNode(leftValue)
        self.left = leftNode

    def setRight(self, rightValue):
        rightNode = BinaryTreeNode(rightValue)
        self.right = rightNode

def allSequences(node):
    res = []
    if not node:
        res.append([])
        return res
    prefix = []
    prefix.append(node.val)
    
    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)

    for left in leftSeq:
        for right in rightSeq:
            weaved = []
            weavedList(left, right, weaved, prefix)
            res.append(weaved)
    return res 

def weavedList(first, second, weaved, prefix):
    if len(first) == 0 or len(second) == 0:
        result = prefix
        result.extend(first)
        result.extend(second)
        weaved.append(result)
        return

    headFirst = first.pop(0)
    prefix.append(headFirst)
    weavedList(first, second, weaved, prefix)
    prefix.pop()
    first.insert(0,headFirst)

    headSecond = second.pop(0)
    prefix.append(headSecond)
    weavedList(first, second, weaved, prefix)
    prefix.pop()
    second.insert(0,headSecond)

def main():
    root = BinaryTreeNode(2)
    root.setLeft(1)
    root.setRight(3)
    sequences = allSequences(root)

    print sequences

if __name__ == "__main__":
    main()
    
    

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None   

    def setLeft(self, left):
        LeftNode = BinaryTreeNode(left)
        self.left = LeftNode

    def setRight(self, right):
        rightNode = BinaryTreeNode(right)
        self.right = rightNode

def checkSubtree(t1, t2):
    str1 = ""; str2 = "";
    getOrderString(t1, str1)
    getOrderString(t2, str2)

    return str2 in str1

def getOrderString(node, s):
    if not node:
        s += "x"
        return 

    s += str(node.val)
    getOrderString(node.left, s)
    getOrderString(node.right, s)

def main():
    r1 = BinaryTreeNode(3)
    r1.setLeft(4)
    r1.setRight(5)
    r1.left.setLeft(1)
    r1.left.setRight(2)

    r2 = BinaryTreeNode(4)
    r2.setLeft(1)
    r2.setRight(2)

    flag = checkSubtree(r1,r2)
    print flag

if __name__ == "__main__":
    main()



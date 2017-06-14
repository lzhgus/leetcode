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

def listDepths(root):
    level = [root]; res = []
    while level and root:
        res.append([node.val for node in level])
        level = [kid for node in level for kid in (node.left, node.right) if kid]
    return res

def listDepths2(root):
    if not root: return []
    res = []
    preOrder(root, res, 0)

def preOrder(root, res, depth):
    if root:
        if len(res) < depth+1: res.append([])
        res[depth].append(root.val)
        preOrder(root.left, res, depth+1)
        preOrder(root.right, res, depth+1)


def main():
    root = TreeNode(1)
    root.setLeft(2)
    root.setRight(3)
    root.left.setLeft(4)
    root.left.setRight(5)
    root.right.setLeft(3)
    root.right.setRight(4)
    root.left.right.setLeft(7)
    print listDepths(root)

if __name__ == "__main__":
    main()

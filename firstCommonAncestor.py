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
    
def commonAncestor(root, p, q):
    parents = {root:None}
    stack = [root]
    while p not in parents or q not in parents:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
            parents[node.left] = node
        if node.right:
            stack.append(node.right)
            parents[node.right] = node

    ancester  = set()
    while p:
        ancester.add(p)
        p = parents[p]

    while q not in ancester:
        q = parents[q]

    return q

def main():
    root = BinaryTreeNode(3)
    root.setLeft(5)
    root.setRight(1)
    root.left.setLeft(6)
    root.left.setRight(2)
    root.right.setLeft(0)
    root.right.setRight(8)
    root.left.right.setLeft(7)
    root.left.right.setRight(4)

    ancestor = commonAncestor(root, root.left.left, root.left.right.left)
    print ancestor.val if ancestor is not None else None

if __name__ == "__main__":
    main()


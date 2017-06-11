class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
    def setLeft(self, leftValue):
        leftNode = BinaryTreeNode(leftValue)
        self.left = leftNode
        if leftNode:
            leftNode.parent = self
    def setRight(self, rightValue):
        rightNode = BinaryTreeNode(rightValue)
        self.right = rightNode
        if rightNode:
            rightNode.parent = self
    
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

def commonAncestorWithParent(root, p, q):
    if (not covers(root,p) or not covers(root,q)):
        return None
    elif covers(p,q):
        return p
    elif covers(q,p):
        return q

    sibling = getSibling(p)
    parent = p.parent
    while (not covers(sibling, q)):
        sibling = getSibling(parent)
        parent = parent.parent
    return parent

def covers(root, p):
    if not root: return False
    if root == p: return True
    return covers(root.left, p) or covers(root.right, p)

def getSibling(node):
    if not node or not node.parent: return None
    parent = node.parent
    return parent.left if parent.right == node else parent.right

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
    
    ancestor2 = commonAncestorWithParent(root, root.left.left, root.left.right.left)
    print ancestor2.val if ancestor is not None else None
if __name__ == "__main__":
    main()


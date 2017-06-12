class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "( " + str(self.val) + " ( " + str(self.left) + " | " + str(self.right) + "))"
# inOrder Traversal, next node will always be the closest node whose value is greater then current node
# so if current node has right subtree, try to find the smallest node in the right subtree
# if current node doesn't has right subtree, try to find the current node's first parent whose value greater than current node
def findNext(node):
    if not node: return None
    if node.right:
        ret = node.right
        while ret.left:
            ret = ret.left
        return ret

    else:
        ret = node.parent
        while ret and ret.val <= node.val:
            ret = ret.parent
        return ret

from random import randrange
def make_randomBST(depth=2, l=-10,r=10,parent=None):
    if depth < 0 or l == r: return None
    tree = BinaryTree(randrange(l,r))
    tree.parent = parent
    tree.left = make_randomBST(depth-1,l,tree.val,tree)
    tree.right = make_randomBST(depth-1,tree.val,r,tree)
    return tree

def in_orderCheck(node):
    if not node: return 
    in_orderCheck(node.left)
    print "current node", node.val
    next_node = findNext(node)
    if not next_node:
        print "next node None"
    else:
        print "next node", next_node.val
    in_orderCheck(node.right)

tree = make_randomBST()
print tree
in_orderCheck(tree)

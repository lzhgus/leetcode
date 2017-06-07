#inorder traversal of bst is the nodes in ascending order, to find a successor jst need to find the smallest one 
#that is larger than the give value 
def inOrder(self, root, p):
    if not root or not p: return None
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ

#1. try to find in p.right subTree
#2. if p's right subTree is empty, go upward, till x.left is p

def inOrder(self, root, p):
    if not root or not p: return None
    if p.right:
        q = p.right
        while q.left:
            q = q.left
        return q
    succ = self.dfs(self, root, p)
    return None if succ == p else succ

def dfs(self, root, p);
    if not root or not p: return None
    left = self.dfs(root.left, p)
    right = self.dfs(root.right, p)
    if right == p:  return p
    if left == p: return root
    return left if left else right

# 3
def inOrder(self, root, p):
    if not root or not p: return None
    if p.right:
        q = p.righ
        while q.left:
            q = q.left
        return q
    else:
        n = p
        x = n.parent
        whiel x and x.left != n:
            n = x
            x = x.parent
        return x 

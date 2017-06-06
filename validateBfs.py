class Solution:
    def validateBst(self, root):
        res = []
        self.inOrder(self, root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]: return False
        return True

    def inOrder(self, root, res):
        if not root: return False
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)


# solution 2 valdiate the tree at the same time doing the inorder traversal 
    def validateBst(self, root):
        cur = None
        return validate(root, cur)

        def validate(root, cur):
            if not root: return False
            if (not validate(root.left, cur)): return False
            if (cur and root.val <= cur):
                return False
            cur = root.val
            if (not validate(root.right, cur)): return False
            return True 

# solution 3 keep track min and max 
    def checkBst(self, root):
        return self.checkBst(self, root, None, None)

    def checkBst(self, root, min, max):
        if not root: return False
        if ((min and root.val <= min) or (max and root.val >= max)):
            return False
        if (not self.checkBst(root.left, min, root.val) or not self.checkBst(root.right, root.val, max)):
            return False
    return True

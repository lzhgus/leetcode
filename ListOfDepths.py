class Solution:
    def listOfDepths(self, root):
        level = [root]; res = []
        while level and root:
            res.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res

    def listOfDepths2(self, root):
        if not root: return []
        res = []
        self.preOrder(root, 0, res)
        return res

    def preOrder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level+1, res)
            self.preOrder(root.right, level+1, res)
        
    # recursive and preOrder dfs

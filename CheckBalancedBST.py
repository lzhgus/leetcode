Class Solution:
    def isBalanced(self, root):
        if not root: return True
        if abs(self.Height(root.left)-self.Height(root.right)) > 1: return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def Height(self, root):
        if not root: return 0
        return max(self.Height(root.left), self.Height(root.right))+1

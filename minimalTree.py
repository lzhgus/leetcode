Class Solution:
    def sortedArrayToBST(self, arr):
        length = len(arr)
        if length == 0: return None
        else if length == 1: return TreeNode(arr[0])

        root = TreeNode(arr[length/2])
        root.left = self.sortedArrayToBST(self, arr[:length/2])
        root.right = self.sortedArrayToBST(self, arr[length/2+1:])
        return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        # 只有右子树
        if not root.left:
            return self.minDepth(root.right) + 1
        # 只有左子树
        if not root.right:
            return self.minDepth(root.left) + 1
        # 左右都存在，取较小值
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

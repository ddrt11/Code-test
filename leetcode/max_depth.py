class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        # 左右子树深度取大的，再加当前这一层
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        return max(left_d, right_d) + 1

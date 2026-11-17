class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return 0
            left_h = dfs(node.left)
            if left_h == -1:
                return -1
            right_h = dfs(node.right)
            if right_h == -1:
                return -1
            # 左右高度差大于1，标记不平衡
            if abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1
        return dfs(root) != -1

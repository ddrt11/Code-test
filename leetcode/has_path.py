class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        # 到达叶子节点，判断是否等于剩余目标
        if not root.left and not root.right:
            return root.val == targetSum
        # 递归左右子树，减去当前节点值
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

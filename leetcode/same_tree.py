class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # 两个节点都为空，相等
        if not p and not q:
            return True
        # 只有一个为空，不相等
        if not p or not q:
            return False
        # 当前值相等，再递归比较左右子树
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

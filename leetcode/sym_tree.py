class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def check(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            # 左子树左 和 右子树右对比；左子树右 和 右子树左对比
            return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)
        return check(root.left, root.right)

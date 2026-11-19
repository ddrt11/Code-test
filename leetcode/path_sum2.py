class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        res = []
        def dfs(node, path, rest):
            if not node:
                return
            path.append(node.val)
            rest -= node.val
            # 叶子节点，并且剩余值为0，找到一条路径
            if not node.left and not node.right and rest == 0:
                res.append(path.copy())
            dfs(node.left, path, rest)
            dfs(node.right, path, rest)
            path.pop()
        dfs(root, [], targetSum)
        return res

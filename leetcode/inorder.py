
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        ans = []  # 保存遍历结果
        def dfs(node):
            if not node:  # 节点为空，终止
                return
            dfs(node.left)       # 遍历左子树
            ans.append(node.val) # 记录当前节点
            dfs(node.right)      # 遍历右子树
        dfs(root)
        return ans

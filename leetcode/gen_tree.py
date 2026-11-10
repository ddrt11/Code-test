
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        # 生成区间 [l, r] 的全部二叉搜索树
        def dfs(l, r):
            tree_list = []
            if l > r:
                return [None] # 区间不存在，返回空
            # 枚举每一个可以作为根的数
            for i in range(l, r + 1):
                left = dfs(l, i - 1)   # 所有左子树
                right = dfs(i + 1, r)  # 所有右子树
                # 左右子树配对组合
                for l_tree in left:
                    for r_tree in right:
                        cur = TreeNode(i)
                        cur.left = l_tree
                        cur.right = r_tree
                        tree_list.append(cur)
            return tree_list
        
        if n == 0:
            return []
        return dfs(1, n)

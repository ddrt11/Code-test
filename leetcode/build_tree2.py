class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        # 后序最后一个元素是根节点
        root_val = postorder[-1]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        # 拆分左右子树数组
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return root

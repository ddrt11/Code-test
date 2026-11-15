class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        # 前序第一个元素是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        # 在中序里找到根的下标，左边是左子树，右边是右子树
        idx = inorder.index(root_val)
        # 拆分左右子树数组，递归构造
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

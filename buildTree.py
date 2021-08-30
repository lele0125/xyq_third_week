# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:return
        root = TreeNode(preorder[0])
        root_inorder_index = inorder.index(preorder[0])
        left_inorder = inorder[:root_inorder_index]
        right_inorder = inorder[root_inorder_index+1:]
        left_preorder = preorder[1:root_inorder_index+1]
        right_preorder = preorder[root_inorder_index+1:]
        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)
        return root
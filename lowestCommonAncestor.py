# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        #迭代
        #跟的左右子树各有p,q则这个根节点为公共祖先
        #根的值为p或q,左右子树里有另一个节点，则根为公共祖先
        # def dfs(root,p,q):
        #     if not root:return False
        #     lson = dfs(root.left,p,q)
        #     rson = dfs(root.right,p,q)
        #     if (lson and rson) or ((root.val==q.val or root.val == p.val) and (lson or rson)) :
        #         self.ans = root
        #     return lson or rson or(root==p or root==q)
        # dfs(root,p,q)
        # return self.ans
        if not root:return None
        if (root.val==p.val) or (root.val==q.val): return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if not left and right:
            return right
        if not right and left:
            return left
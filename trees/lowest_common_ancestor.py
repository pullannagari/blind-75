# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val:
            if self.dfs(root.left, q) or self.dfs(root.right, q):
                return root
            return None
        elif root.val == q.val:
            if self.dfs(root.left, p) or self.dfs(root.right, p):
                return root
            return None
        else:
            if (p.val < root.val < q.val) or (q.val < root.val < p.val):
                return root
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return None


    def dfs(self, root, curr):
        if not root:
            return
        if not curr:
            return
        if root.val < curr.val: 
            return self.dfs(root.right, curr)
        elif root.val > curr.val:
            return self.dfs(root.left, curr)
        else:
            return root
        
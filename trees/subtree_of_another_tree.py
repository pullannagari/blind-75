# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            if self.dfs_structure_match(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif root:
            return True
        elif subRoot:
            return False
        else:
            return True

    def dfs_structure_match(self, root, subroot):
        if root and subroot:
            if root.val == subroot.val:
                if self.dfs_structure_match(root.left, subroot.left) and self.dfs_structure_match(root.right, subroot.right):
                    return True
            return False
        elif root:
            return False
        elif subroot:
            return False
        else:
            return True
        
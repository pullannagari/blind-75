from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min = float("-inf")
        max = float("+inf")

        def valid_helper_new(node, min, max):
            if not node:
                return True
            if not (node.val > min and node.val < max):
                return False
            return valid_helper_new(node.left, min, node.val) and valid_helper_new(node.right, node.val, max)
        
        return valid_helper_new(root, min, max)
        
    def valid_helper(self, curr, min, max):
        if not curr:
            return True
        left = True
        right = True
        if curr.left:
            if curr.left.val < curr.val and curr.left.val > min:
                left = self.valid_helper(curr.left, min, curr.val)
            else:
                return False
        if curr.right:
            if curr.right.val > curr.val and curr.right.val < max:
                right = self.valid_helper(curr.right, curr.val, max)
            else:
                return False
        return left and right
    
        
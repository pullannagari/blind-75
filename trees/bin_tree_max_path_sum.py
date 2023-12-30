from typing import Optional

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.max = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = root.val
        self.max_path_helper(root)
        return self.max

    def max_path_helper(self, curr):
        if not curr:
            return 0
        left = self.max_path_helper(curr.left)
        right = self.max_path_helper(curr.right)
        left_max = max(left, 0)
        right_max = max(right, 0)

        # with splitting, meaning the path is only included from the current node
        self.max = max(self.max, left_max + curr.val + right_max)

        # return without splitting
        return curr.val + max(left_max, right_max)
        
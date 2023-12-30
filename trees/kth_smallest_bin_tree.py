from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # result_arr = []
        # self.pre_order(root, result_arr)
        # return result_arr[k-1]
        return self.kthSmallest_iterative(root, k)
    
    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

    
    def pre_order(self, curr, result):
        if not curr:
            return
        self.pre_order(curr.left, result)
        result.append(curr.val)
        self.pre_order(curr.right, result)
                    
        

                    



        
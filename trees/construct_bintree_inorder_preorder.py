from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        if len(inorder) == 1:
            return TreeNode(val=inorder[0])
        else:
            root = TreeNode(val=preorder[0])
            for i, v in enumerate(inorder):
                if v == root.val:
                    inorder_index = i
                    break
            left_inorder = inorder[:inorder_index]
            right_inorder = inorder[inorder_index+1:]
            left_preorder = preorder[1:1+len(left_inorder)]
            right_preorder = preorder[1+len(left_inorder):]
            root.left = self.buildTree(left_preorder, left_inorder)
            root.right = self.buildTree(right_preorder, right_inorder)
            return root
        
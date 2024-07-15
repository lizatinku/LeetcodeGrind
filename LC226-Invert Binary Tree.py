# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# check the base case when root is null
# set temp to be the left root
# set left root to be the right root
# set right root to be the temp root
# do the recursive case next
# invert the subtrees - left and right
# return the root 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive case
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

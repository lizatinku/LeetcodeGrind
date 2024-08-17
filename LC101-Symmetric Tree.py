# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# use a helper function
# base case:
#   if left subtree and right subtree is empty, it is symmetric
#   if either left or right is empty, it is not symmetric
#   if the value on left is not equal to the value on the right, it is not symmetric
# Recursive case
#   call the function on all the corresponding mirror positions of the subtree
#   call the function and pass the left and right roots

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root, root)

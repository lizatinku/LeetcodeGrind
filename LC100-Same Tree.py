# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# Overall, we need to check if structures are same and value at each node is the same
# base case:
#   if both trees are none, then it is identical
#   if either of them is none, then it is not identical
#   if both trees are not null, then we check the values of the current nodes are the same or not
# recursive case
# call the function on left subtrees of p and q
# call the function on right subtree of p and q

# Concepts:
# DFS: for recursive binary tree problems, a Depth First Search is used.  It starts from the root and explores as far as possible along each branch before backtracking. Usage in Trees: In recursive binary tree problems, DFS is used because it explores each node and its subtrees in a systematic manner.
# We still need to call the function recursively even after checking p.val != q.val is to ensure that not only the current nodes are identical but also that the entire structure and values of the subtrees are the same.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))

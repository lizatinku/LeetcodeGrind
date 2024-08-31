# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# My plan
# have a helper function
# Base case:
#   if the current node is none, then return none
# Recursive case
# check if the value of p and q is less than the node, then LCA is in the left subtree
# check if the value of p and q is greater than the node, then  LCA is in the right subtree
# now, if both conditions don't satisfy we know that the current node is the LCA
# call the helper function passing the root

# Concept:
# In a BST, the left subtree of a node contains only nodes with values less than the node's value.
# The right subtree contains only nodes with values greater than the node's value.

# LCA Conditions:
# If both p and q are smaller than the current node’s value, the LCA must be in the left subtree.
# If both p and q are larger than the current node’s value, the LCA must be in the right subtree.
# If p and q are on opposite sides of the current node (one is smaller, and one is larger), or one of them equals the current node, then the current node is the LCA.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node is None:
                return None
            
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node

        return dfs(root)
        

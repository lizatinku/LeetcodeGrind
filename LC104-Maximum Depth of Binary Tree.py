# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# base case is if it's not a node, return none
#   The depth of a tree is the number of edges on the longest path from the root to a leaf. If a node does not exist (i.e., it is None), it contributes 0 to the depth because there are no edges.
# use a helper function
# call the function recursively on the right and left subtrees
# use the max function to compare both heights
#   include + 1 to account for the current node in the depth calculation
# return the result

# Concepts:
# 1. Passing node in function definition but root in function call: This is a common pattern in recursive functions to separate the initial function call (with the tree's root node) from the recursive logic that processes each individual node.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if node == None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            return max(left_height, right_height) + 1

        return dfs(root)

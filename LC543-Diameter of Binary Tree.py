# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# Use a list to store the maximum diameter found during traversal.
# define a helper function and pass the root node as parameter
# base case:
#   if the node is null, its depth is -1
# for the recursive case:
#   Traverse the left subtree by calling dfs on the left child.
#   Traverse the right subtree by calling dfs on the right child.
# update the diameter at each node by comparing the current diameter with the sum of the depths of the left and right subtrees.
# for each node, return the maximum depth of its subtrees.
# call the function
# return the computer diameter  stored in result[0]

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            result[0] = max(result[0], 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return result[0]

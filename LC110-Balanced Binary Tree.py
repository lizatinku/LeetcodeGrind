# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# define a function to call it recursively
# base case: if it's a node, it is considered balanced and height is 0
# recursive case
#   check the balance status and height of left subtree 
#   check the balance status and height of right subtree 
#   check if the difference in height between the left and right subtrees is no more than 1.
# return a list with 2 elements
#   Element 1: whether the current subtree is balanced.
#   Element 2: the height of the current subtree.
# Call the recursive function on the root of the tree.


# Concepts learned
# Depth-First-Search: A tree traversal technique where you explore as far down a branch as possible before backtracking. DFS is used here to traverse the tree and evaluate each subtree recursively.

# Recursive Tree Traversal: Using a recursive approach to explore each node of the tree. In this case, the tree is traversed to evaluate the balance and height of each subtree.

# Balance condition: A binary tree is considered balanced if, for every node, the height difference between its left and right subtrees is no more than one.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return [balanced, 1 + max(left_height, right_height)]

        return dfs(root)[0]

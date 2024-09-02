# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# use a helper function and pass both trees as arguments
# if both trees are empty, then they are similar
# if either one of them is empty, we compare the trees for the corresponding values

# use another helper function and pas the node as an parameter
# base case: if it is not a node, return nothing
# call the same tree function and pass the whole tree and the subroot
# recursive case
#   call the 2nd helper function and pass right and left subtrees
# call the 2nd helper function and pass the whole tree

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(s, t):
            if not s and not t:
                return True
            
            if s and t and s.val == t.val:
                return (same_tree(s.left, t.left) and
                        same_tree(s.right, t.right))
            
            return False
        
        
        def dfs(node):
            if not node:
                return False
            
            if same_tree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

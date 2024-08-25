# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My plan
# use a helper function and pass left and right subtrees
# base case:
#   if left is greater than right, it means there are no elements left in the subarray to form a node, so return None.
# calculate the middle index of the current subarray.
# recursive case:
#   call the helper function to construct the left subtree
#   call the helper function to construct the right subtree
# return the root
# call the helper function and pass array from index 0 to end of array

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildBST(left, right):
            if left > right:
                return None

            mid = (left + right)//2
            root = TreeNode(nums[mid])

            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)

            return root

        return buildBST(0, len(nums)-1)

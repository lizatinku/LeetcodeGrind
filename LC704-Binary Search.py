# My plan
# use enumerate to loop through every value and its index of the array
# search for target using an if statement
# if found, return the index
# if not found, return -1

# Concepts:
# Enumerate: A built-in function that adds a counter to an iterable and returns it as an enumerate object. This object can be used directly in for loops to get both the index and the value of each element.
# -1: -1 is better than returning False when something is not found in the array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value == target:
                return index
        return -1

nums = [-1, 0, 3, 5, 9, 12]
sol = Solution()

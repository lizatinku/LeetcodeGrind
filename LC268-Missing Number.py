# My plan
# initialize a counter for result which will store the difference between the expected sum of numbers and the actual sum of numbers
# iterate through nums using a for loop
# i is the expected value at index i if no number were missing, nums[i] is the actual value at index i in the given array.
# the missing number is found by subtracting the actual sum from the expected sum.
# return the result

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        return result

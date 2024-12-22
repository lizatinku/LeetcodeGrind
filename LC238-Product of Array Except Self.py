# My plan
# create 2 arrays called suffix and prefix
# Building the prefix array: 
#   iterate the array nums using a for loop from left to right
#   multiply with everything before the number and the current number. Eg: In (1,2, 3, 4), if we are at 2, multiply it with 2 * 1 = 2. 
# Building the suffix array: 
#   iterate the array nums using a for loop from right to left
#   multiply with everything after the number and the current number. Eg: In (1,2, 3, 4), if we are at 2, multiply it with 2 * 3 * 4 = 24. 
# combine both arrays
# return the combined array

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n  
        suffix = [1] * n 

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = [prefix[i] * suffix[i] for i in range(n)]

        return result

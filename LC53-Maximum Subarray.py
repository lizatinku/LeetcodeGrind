# My plan
# create a array and have the first value in the array to be maximum subarray
# have a empty counter for current sum
# iterate through the array using a for loop
# while iterating, check if the current sum is less than 0,
#   if it yes, set the current sum to be 0 as it lowers the value of the subarray
#   note: if we encounter a negative after a positive but negative + positive = positive, we include that negative in the subarray
#   else, add the current element to the current sum
# the maximum subarray will be a maximum of and maximum subarray and the current sum 
#   By comparing maximum subarray and current sum during each iteration, we ensure that maximum subarray always holds the highest possible subarray sum.
# return the maximum subarray


# Concepts learnt:
# 1. Sliding window: Initially I have a window. called current sub array and it is set to 0, As I iterate throught the array, I slide the window by adding the current element n to current_sum. The window continues to slide through the array, either expanding by including more elements or resetting whenever a negative sum is encountered, until I've considered all possible subarrays.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sub = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sub = max(max_sub, current_sum)
        return max_sub

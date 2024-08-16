# My plan
# initialize a pointer to be at the start of the array
# iterate through the array using a for loop
# check if the current element is a non-zero
#      if it yes, swap the current value in the array with the 0
# increment the start pointer

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for item in range(len(nums)):
            if nums[item]:
                nums[start], nums[item] = nums[item], nums[start] 
                start += 1 

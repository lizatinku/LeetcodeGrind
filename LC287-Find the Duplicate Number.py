# My plan
# input is an array of integers containing n+1 integers
# output is an integer that is duplicated in the array
# we can use Floyd's algorithm for this

# Part 1 - Cycle detection
# we initialize 2 pointers, slow and fast, both starting at the first element of the array (nums[0])
# we iterate until the end of the array
# move slow pointer by 1 step, move fast pointer by 2 steps
# when slow and fast meet, there is a cycle and we break the loop 

# Part 2 - Finding duplicate
# once the cycle is detected, have a 3rd pointer which is initialized at the start of the array nums[0]
# we iterate again until the end of the array
# move the slow pointer and the slower pointer by 1 step at a time
# Return the value at the meeting point of both slow & slower pointers which is the duplicate number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slower = nums[0]
        while slow != slower:
            slow = nums[slow]       
            slower = nums[slower]     

        return slow
        

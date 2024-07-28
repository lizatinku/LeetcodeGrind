# My plan
# initialize an empty dictionary
# iterate through the nums array using a for loop
# if it is already in the hashmap
#   return true
# if not, add to the hashmap
# if the loop finishes without any duplicates, return false 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_store = {}
        for i in nums:
            if i in num_store:
                return True
            else:
                num_store[i] = 1
        return False

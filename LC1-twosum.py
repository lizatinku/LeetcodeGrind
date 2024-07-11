# My plan
# initialize an empty dictionary for storing the index of elements
# we need a for loop to go through the array through both the index and the value 
# when approaching a new element, find the difference by doing subtracting the target from the current element
# check if this difference exists in the dictionary and if it does, return the indice of the value in dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_store = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in index_store:
                return [index_store[difference], index]
            index_store[value] = index

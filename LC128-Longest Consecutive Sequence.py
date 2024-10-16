# My plan
# input is an array, output is an integer
# we want to make the longest sequence from the numbers given in the array - it doesn't matter where in the array the numbers are in currently
# we pass the array into a set constructor to convert into a set
# initialize a variable for the longest sequence found
# iterate through every number in the input list
# check if current number is the start of the sequence
#   if yes, initialize the length counter
# count elements starting from i
# keep a track of the length of the sequence
# return the length of the longest sequence found

# Tips
# We convert from an array to a set primarily for the benefits of fast membership testing and handling unique elements, rather than any property of order. 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_set = set(nums)
        longest_sequence = 0

        for i in nums:
            if (i-1) not in new_set:
                length = 0
                while (i + length) in new_set:
                    length += 1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence

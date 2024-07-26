# My plan
# have an empty hashmap
# Initialize a variable to 0 to keep track of the highest count.
# iterate the array using a for loop
#   if item already in hashmap, increment it
#   else, add it with a count of 1
# compare the current count with an if statement
# if the current count is greater than the stored count:
#   update the count
#   update the most repeated element
# return the most repeated element

# Concepts:
# A hashmap (or dictionary) is used to store the frequency of each element in the array. This allows for efficient insertion and lookup operations.


# O(n) solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num_store = {}
        count = 0
        most_repeated_element = None

        for item in nums:

            if item in num_store:
                num_store[item] += 1
            else:
                num_store[item] = 1

            if num_store[item] > count:
                count = num_store[item]
                most_repeated_element = item
            
        return most_repeated_element


#O(1) solution or Boyer-Moore Voting Algorithm:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

      result = 0 
      count = 0
      
      for i in nums:
        if count == 0:
          result = n
          count += (1 if i == result else -1)
      return result
        

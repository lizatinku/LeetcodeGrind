# My plan
# have an empty hashmap
# iterate the array using a for loop
# if element not in the hashmap, add to the hashmap
# if element in the hashmap, increment it
# iterate the array using another for loop
# using an if statement, see if the count if 1 for any elemnt
#   if yes, return that element

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashmap = {}
        count = 0

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for num in hashmap:
            if hashmap[num] == 1:
                return num


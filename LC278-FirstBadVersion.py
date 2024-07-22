# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# My plan
# Initialize 2 pointers called low and high 
# Low will be at the start of the range, high will be at the end
# result is initialized to -1: If there are no bad versions in the range, the algorithm will complete without updating result.  
# iterate the range using a while loop, this will loop as long as low is less than or equal to high
# initialize a new variable called middle which is low + high // 2
# call the API and pass the middle varible to see if bad version is in the middle
#   if it is, move the high pointer to search in the left half
#   if it is, the result will be mid
#   if not, move the low pointer to search in the right half
# After the loop, return the result which has the bad version.

# Concepts:
# Binary search: works by dividing the search range in half each time, which significantly reduces the number of elements to consider. By always checking the middle point, you effectively halve the search space, leading to a time complexity of O(log n). This is much faster than a linear search, which has a time complexity of O(n).

# Adjusting the pointers: Checking the middle point first ensures that you can quickly eliminate half of the remaining search space in each step. If the middle version is bad, we know the first bad version must be before this point, so we adjust the high pointer. If it's not bad, we know the first bad version must be after this point, so we adjust the low pointer.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        

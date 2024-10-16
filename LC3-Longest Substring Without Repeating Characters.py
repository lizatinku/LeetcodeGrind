# My plan
# initialize an empty set
# set a left pointer as the start of the window
# iterate the range of the string using a for loop 
# iterate as long as the same char is not in the set
#   removing characters from the set 
#   Move the left pointer i to the right
# Add the character at j to the set
# Update the counter with the maximum of the counter and current length of the substring
# Return the counter

# Key points:
# Set: Set is a DSA that can only contain 1 of each character
# Sliding window: 
# O(n) is the time and space complexity by using a sliding window technique. 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        counter = 0
        new_set = set()
        i = 0

        for j in range(len(s)):
            while s[j] in new_set:
                new_set.remove(s[i])
                i += 1
            
            new_set.add(s[j])
            counter = max(counter, j - i + 1)
        return counter

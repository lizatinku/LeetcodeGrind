# My plan
# make an empty hashmap to store the frequency of each character
#   use defaultdict(int) from the collections module to handle this efficiently.
# initialize a result variable which will store the longest palindrome
# iterate through s using a for loop
# add each character to the hashmap
# check if the count of each character is 2. If it is, add 2 to the result variable.
#   This check to see if the character count is even so sufficient char pairs can be formed.
# use a for loop to iterate through the hashmap
#   count.values() returns a view of frequencies of all characters stored in the count dictionary.
# Now, check if the character count is odd. This odd-count character can be used as the center of the palindrome, while the rest of the characters form pairs around it.
# the loop is broken to stop further checking
# the result(length of the longest possible palindrome) is returned 

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = defaultdict(int)
        result = 0

        for char in s:
            count[char] += 1
            if count[char] % 2 == 0:
                result += 2

        for c in count.values():
            if c % 2:
                result += 1
                break

        return result

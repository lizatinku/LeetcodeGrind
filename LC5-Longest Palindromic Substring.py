# My plan
# set the result to be an empty string
# initialize a variable for the length of the string
# iterate through the word using a for loop
# for odd words
# set 2 pointers at the start of the word
# Expand outward
# Update result if longer palindrome found
# decrement the left pointer
# increment the right pointer

# for even words
# Set two pointers at current and next character
# Expand outward
# Update result if longer palindrome found
# decrement the left pointer
# increment the right pointer

# Return the longest palindromic substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result = s[l:r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1

            # Even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result = s[l:r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1

        return result

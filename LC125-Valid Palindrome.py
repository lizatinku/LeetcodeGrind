# My plan
# pointer at start, pointer at end
# while loop comparing as long as start is less than end
# edge case is when a character is a space. 
# increment start pointer when it encounters a space to skip the space
# decrement end pointer when it encounters a space to skip the space
# if string character at start is not equal to string character at end, return False
# increment start pointer, decrement end pointer
# If the loop completes without finding any mismatch, return True.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True

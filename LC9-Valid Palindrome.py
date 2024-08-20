# My plan
# convert x into a string
# have a pointer at the start, have a pointer at the end
# have a while loop that iterates as long as start is not equal to end
# have an if statement saying if start does not match the end, then return false
# increment the start pointer, decrement the end pointer
# return true outside the loop

class Solution:
    def isPalindrome(self, x: int) -> bool:

        string = str(x)

        start = 0
        end = len(string) - 1

        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True
        

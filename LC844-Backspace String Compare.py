# O(1) solution
# use a helper function and pass a string and its index
# initialize a counter for the backspace
# iterate as long as the index is greater than 0
#   if char is a #, increment the backspace counter
#    If the character is not # and the backspace counter is greater than 0, decrement the backspace counter.
#   else, break out of the loop
# Decrement the index in each iteration.
# return the updated index afetr the loop
# initialize 2 pointers to the end of the string
# Iterate as long as either pointer is valid (greater than or equal to 0).
# Call helper function for both strings with their respective indices to get the next valid character positions.
# Compare the characters at these valid positions. If the characters are not equal, return False
# Decrement both pointers to move to the next character positions
# using an if statement, compare both string 1 and string 2
#  If the loop completes without finding any unequal characters, return True.
# else, return false

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def next_valid_char(string, index):
            backspace = 0
            while index >= 0:
                if string[index] == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                else:
                    break
                index -= 1
            return index

        index_s = len(s) - 1
        index_t = len(t) - 1

        while index_s >= 0 or index_t >= 0:
            index_s = next_valid_char(s, index_s)
            index_t = next_valid_char(t, index_t)

            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""

            if char_s != char_t:
                return False
            
            index_s -= 1
            index_t -= 1

        return True

# My plan
# create a empty string that will store the longest common prefix.
# iterate through each character in the 1st string using a for loop
# have a nested for for loop to compare the 1st character of string 1 to 1st character of string i
# If any string has a different character at index i
#   or Edge case: if the index i exceeds the length of the string
# stop the comparison and return the result string
# return the result string which has the longest substring

# Concepts used
# 1. String Comparison: The code relies on comparing characters at the same index across multiple strings. This concept is fundamental in checking whether a group of strings shares a common prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result

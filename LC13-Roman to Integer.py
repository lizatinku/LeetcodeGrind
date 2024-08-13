# My plan
# make a hashmap with symbols and their values
# initialize an empty counter for output
# initialize a varaible to keeps track of the current position in the string 
# iterate the string as long as i is less than the length of the string
# if: a) ensure that i + 1 is a valid index within the string s and whether there is a next character to consider.
# b) check if the current value in hashmap is less than the previous value in the hashmap
#   subtract the corresponding values in the hashmap and add to output
#   increment by 2 to move past this pair
# Else, add the correspondidg value in the hashmap to the output
# return the output

# Concepts:
# map[i] vs map[s[i]]
# Example with a list
# values = [10, 20, 30, 40]
# i = 2
# print(values[i])  # Output: 30

# # Example with a dictionary
# map = {0: 'zero', 1: 'one', 2: 'two'}
# print(map[i])  # Output: 'two'


class Solution:
    def romanToInt(self, s: str) -> int:

        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and map[s[i]] < map[s[i + 1]]:
                output += map[s[i + 1]] - map[s[i]]
                i += 2 
            else:
                output += map[s[i]]
                i += 1
        return output


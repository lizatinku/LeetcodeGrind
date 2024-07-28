# My plan
# have an dictionary with each symbol mapped to its value
# have an empty variable for output and for previous value
# iterate the string s using a for loop
# add every char of the string to the dictionary 
# if the current value is greater than the previous value:
#   2 times the previous value is subtracted from the current value and added to the output
#   For IX, output = 1 + 10 - 2 * 1 = 1 + 10 - 2 = 9
# if not, just add the current value to the output
# the previous value is now set to be the current value
# return the output string

class Solution:
    def romanToInt(self, s: str) -> int:

        symbol_and_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = 0
        prev_value = 0 

        for char in s:
            current_value = symbol_and_value[char]
            if current_value > prev_value:
                output += current_value - 2 * prev_value
            else:
                output += current_value
            prev_value = current_value
        return output       

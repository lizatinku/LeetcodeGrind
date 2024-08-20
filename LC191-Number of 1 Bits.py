# My plan
# initialize a variable for result and set to 0 to start the count of '1' bits
# iterate as long as n is non-zero
# append the result 
#   by adding n divided by 2 if the least significant bit is 1
#   else, add 0 if the least significant bit is 0
# shifts n one bit to the right, thereby removing the least significant bit
# return the result

# Concepts used:
#1. Bitwise Operations: Right Shift (>>): This operation shifts the bits of the integer n to the right by one position. It effectively removes the least significant bit and divides the number by 2. This is used in the code to iterate through each bit of the integer.

class Solution:
    def hammingWeight(self, n: int) -> int:

        result = 0

        while n:
            result += n % 2
            n = n >> 1
        return result

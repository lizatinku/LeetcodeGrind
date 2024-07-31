# My plan
# create a list with size n + 1, to store number of 1's from 0 to n
# initialize a variable offset to identify the most significant bit position in i
# iterate through with a for loop
# If i is a power of 2, update the offset to i. This is because the number of 1's resets at each power of 2.
# Calculate the number of 1's in the binary representation of i and store i in the list 
# return the list after the loop

class Solution:
    def countBits(self, n: int) -> List[int]:
        new_list = [0] * (n + 1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            new_list [i] = 1 + new_list [i - offset]
        return new_list 

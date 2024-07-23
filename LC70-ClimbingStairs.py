# My plan
# Base cases
#   pointer1 to represent the number of ways to reach the current step.
#   pointer2 to represent the number of ways to reach the previous step.
#   iniitialize both to 1 becuase there is only one way to reach the first and second step

# iterate using a for loop
# use the swapping technique
#   store pointer1 in temp
#   set p1 to be a sum of one and two
#   set p2 to be the value in temp
# return pointer1 as one will contain the number of ways to reach the nth step.

class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1
        for i in range(n-1):

            temp = p1
            p1 = p1 + p2
            p2 = temp

        return p1


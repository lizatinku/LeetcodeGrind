# My plan
# initialize a list for output
# initialize a variable for carry
# in addition, we start from thr right-most digit, so same logic to add binary strings
# iterate over the maximum length of the two binary strings
# add corresponding bits from both strings if available
# append the result bit
# If there's a carry left, append it
# Reverse the result and join the output to get the correct order

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        output = []
        carry = 0

        a = a[::-1]  
        b = b[::-1]
        
        
        for i in range(max(len(a), len(b))):
            bit_sum = carry

            if i < len(a):
                bit_sum += int(a[i])
            if i < len(b):
                bit_sum += int(b[i])
            
            output.append(str(bit_sum % 2))
            carry = bit_sum // 2
        
        if carry:
            output.append('1')
        
        return ''.join(output[::-1])

# My PLAN
# have a dictionary to hold all the brackets as key and value
# have an empty stack
# iterate through the string using a for loop
# check if each character's key/value in the string is there in the bracket map
# if it matches, pop the element
# check if the popped element matched what is there in bracket
# If not, return False. If yes, just continue
# if char not in bracket map, append the stack with the character


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            
            if char in bracket_map:
                popped_element = stack.pop() if stack else '%'
                if bracket_map[char] != popped_element:
                    return False
            else:
                stack.append(char)

        return not stack

sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}")) 
print(sol.isValid("(]"))



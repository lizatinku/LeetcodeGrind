# My plan

# create an empty hashmap to store the letters
# iterate through magazine using a for loop
# using an if statement, check if the letter is in the hashmap already
#   if yes, increment it
#   # if not, add it with a count of 1
# iterate though ransomnote using a for loop
# using an if statement, check if the letter is not in the hasmap
#   if not, return false
#   If the letter count is 1, delete it from the hashmap
#   Otherwise, decrement the count
# return true if all letters in the ransom note are successfully matched


# Concepts:
# 1) A hashmap, known as a dictionary in Python, is a data structure that stores key-value pairs. In this context, the keys will be the letters from the magazine and the values will be the counts of each letter. This allows for efficient storage and retrieval of the letter counts.
# 2) Key Operations: Insertion:, Lookup, Deletion

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        letter_store = {}
        
        for i in magazine:
            if i in letter_store:
                letter_store[i] += 1
            else:
                letter_store[i] = 1

        for i in ransomNote:
            if i not in letter_store:
                return False
            elif letter_store[i] == 1:
                del letter_store[i]
            else:
                letter_store[i] -= 1
        
        return True

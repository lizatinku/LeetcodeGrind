# My plan
# have an empty dictionary
# edge case is when len of both strings are not the same
# create 2 empty hashmaps
# for loop through string s
# add each i of string s to the hashmap 
# add each i of string t to the hashmap 
# for an edge case do the .get function incase the hashmap is empty
# for loop through the 1st hashamp
# compare the characters in both hashmaps
# return False if every char in hashmap1 does not match hashmap2
# return True otherwise

# Concept
# nested_dict = {
#     'car': {'c': 1, 'a': 1, 'r': 1},
#     'rat': {'r': 1, 'a': 1, 't': 1}
# }

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        
        for char in hashS:
            if hashS[char] != hashT.get(char, 0):
                return False
        
        return True

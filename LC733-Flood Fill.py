# My plan
# Initialize variables for starting color at image's sr and sc
# Edge case: if the starting color is the same as the new color, no need to proceed
# define a function with parameters for recursive case
# there are 3 base cases:
#   If the current position is out of bounds, return.
#   If the current position already has the new color, return.
#   If the current position does not have the starting color, return.
# for recursive case: apply the color up, down, left and right
# Call the recursive function starting from (sr, sc).
# Return the updated Image


# Concepts:
# DFS: The flood fill algorithm can be seen as a form of DFS, where we explore as far as possible along each branch before backtracking. 
#Base case: The condition under which the function stops calling itself to prevent infinite recursion. 
#Recursive case: The part of the function where it calls itself with modified parameters.
# len(image[0]) for the y-axis (columns) and len(image) for the x-axis (rows) is due to how 2D arrays (or lists of lists) are structured in Python.


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]
        
        def flood_fill(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != start_color: return
            
            image[x][y] = color
            
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)
        
        flood_fill(sr, sc)
        return image

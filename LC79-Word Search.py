# My plan
# set the length of the board to be the number of rows and columns
# Initialize path as a set to keep track of cells visited during a depth-first search (DFS)
# define a helper function to do a depth first search 
# Base condiiton: if our current length matches the required length, return true
# then, check a couple of things
#   if it is out of bounds or not
#   contains a character different from word[i].
#   already in the path set, indicating we’ve visited it before in the current search.
# Recursively call dfs in each of the four directions:
    # Down: dfs(r + 1, c, i + 1)
    # Up: dfs(r - 1, c, i + 1)
    # Right: dfs(r, c + 1, i + 1)
    # Left: dfs(r, c - 1, i + 1)
# Remove row & column from path to allow other search paths to use this cell.
# iterate the rows using a for loop, have a nested for loop and iterate the columns
# call the helper function and if it is true, return true as we found the word
# return false otherwise

# Techniques used:
# Backtracking:is a technique used to explore all possible solutions by building a solution incrementally and abandoning ("backtracking") as soon as we determine that a partial solution cannot lead to a valid solution.
#   The algorithm searches for a sequence of characters that match the word in the grid.
#   Starting from any cell, we try to build the path by adding characters in sequence.
#   If we reach a cell where we can't continue the word (either due to bounds, incorrect characters, or revisiting cells), we backtrack: we "undo" the last step by removing that cell from the path and trying the next possible option.

# DFS(Depth First Search): is a graph traversal technique where we start at a node (cell, in this case) and explore as far down one path as possible before backtracking.
# For each cell (r, c): DFS searches deeper into one direction (e.g., r+1, c) before moving to the next, making it ideal for exploring word paths.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r>= rows or c>=cols or word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

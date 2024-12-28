# My plan
# initialize number of rows to be the length of the matrix
# initialize the number of columns (cols) as the length of the first row in the matrix
# iterate through the 1st column & if any element is 0, set a row flag to true
# iterate through the 1st row & if any element is 0, set a column flag to true
# Check the rest of the matrix (excluding the first row and first column) for 0's and mark the corresponding 
#   cells in the first row and first column as 0.
# Iterate through the matrix again, starting from the second row and second column:
#   For each cell, if the corresponding cell in the first row or first column is 0, set the cell to 0
# If flag for first row is true, iterate through all columns and set the first row to 0.

# In simple words, check: first row for 0's, first column for 0's, second rows & columns are 0's and put flags if they have 0's. Then, change cells to zeros based on the markers, do a final check. 
# Special: this code beats 100% people in efficiency :)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        firstRowHasZero = False
        firstColHasZero = False

        for row in range(rows):
            if matrix[row][0] == 0:
                firstColHasZero = True
                break

        for col in range(cols):
            if matrix[0][col] == 0:
                firstRowHasZero = True
                break

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if firstColHasZero:
            for row in range(rows):
                matrix[row][0] = 0

        if firstRowHasZero:
            for col in range(cols):
                matrix[0][col] = 0


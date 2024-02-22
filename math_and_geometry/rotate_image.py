from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = cols = len(matrix)

        for row in range(rows):
            for col in range(row, cols):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        for row in range(rows):
            matrix[row] = matrix[row][::-1]
        
        return matrix

        
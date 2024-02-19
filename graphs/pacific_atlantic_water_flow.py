from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        result = []
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(row, col, visited, prev):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if (row, col) in visited:
                return
            if prev > heights[row][col]:
                return
            visited.add((row, col))
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                dfs(nr, nc, visited, heights[row][col])

        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        for r in range(len(heights)):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result
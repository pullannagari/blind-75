from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        viset = set()
        def dfs(r, c):
            if r < 0 or c < 0:
                return
            if r >= row or c >= col:
                return
            if visited[r][c]:
                return
            if grid[r][c] != "1":
                return
            visited[r][c] = True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        def bfs(r_in,c_in):
            queue = deque()
            queue.append((r_in,c_in))
            viset.add((r_in,c_in))
            while queue:
                r , c = queue.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(row) and nc in range(col):
                            if (nr, nc) not in viset and grid[nr][nc] == "1":
                                queue.append((nr,nc))
                                viset.add((r,c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not visited[r][c]:
                    result += 1
                    dfs(r,c)
        return result
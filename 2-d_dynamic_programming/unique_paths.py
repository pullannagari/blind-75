class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dfs memoization using dp
        # dp = {}
        # visited = set()
        # def dfs(row, col):
        #     if (row, col) in dp:
        #         return dp[(row,col)]
        #     if row >= m or col >= n:
        #         return 0
        #     if (row,col) in visited:
        #         return 0
        #     if row == m-1 and col == n-1:
        #         return 1
        #     directions = [(1,0), (0, 1)]
        #     visited.add((row,col))
        #     result = 0
        #     for d in directions:
        #         dr, dc = d
        #         nrow = row + dr
        #         ncol = col + dc
        #         result += dfs(nrow, ncol)
        #     visited.remove((row,col))
        #     dp[(row,col)] = result
        #     return dp[(row,col)]
        # return dfs(0,0)

        # using tabulation 
        mat = [[0]*n for _ in range(m)]
        for i in range(n):
            mat[m-1][i] = 1
        for i in range(m):
            mat[i][n-1] = 1
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                mat[row][col] = mat[row+1][col] + mat[row][col+1]
        return mat[0][0]
            



        #     visited.remove((row,col))
        # dfs(0,0,"")
        # return len(uniques)


        



        
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # tabulation
        m = len(text1) + 1
        n = len(text2) + 1
        mat = [[0]*n for _ in range(m)]
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                if text1[row] == text2[col]:
                    mat[row][col] = 1 + mat[row+1][col+1]
                else:
                    mat[row][col] = max(mat[row][col+1], mat[row+1][col])
        return mat[0][0]
                


        # recursive memoization solution
        # dp = {}
        # def dfs(index1, index2):
        #     if (index1, index2) in dp:
        #         return dp[(index1, index2)]
        #     if index1 >= len(text1):
        #         return 0
        #     if index2 >= len(text2):
        #         return 0
        #     result = 0
        #     if text1[index1] == text2[index2]:
        #         result = 1 + dfs(index1+1, index2+1)
        #     else:
        #         result = max(dfs(index1+1, index2), dfs(index1, index2+1))
        #     dp[(index1, index2)] = result
        #     return dp[(index1, index2)]

        # return dfs(0, 0)
        
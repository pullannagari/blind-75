from typing import List

class Solution:

    
    def canJump(self, nums: List[int]) -> bool:

        # greedy method which results in O(n) solution
        length = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= length:
                length = 0
            length += 1
        return length == 1

        # using dynamic programming memoization
        # dp = {}
        # def dfs(index):
        #     if index in dp:
        #         return dp[index]
        #     if index == len(nums)-1:
        #         return True
        #     elif index >= len(nums):
        #         return False
        #     for i in range(nums[index], 0, -1):
        #         if dfs(i+index):
        #             dp[index] = True
        #             return True
        #     dp[index] = False
        #     return False

        # return dfs(0)
        
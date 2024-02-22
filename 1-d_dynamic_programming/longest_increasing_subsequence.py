from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # using dynamic programming tabulation
        dp = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)



        # dp = {}
        # def dfs(index, prev):
        #     if index >= len(nums):
        #         return 0
        #     if (index, prev) in dp:
        #         return dp[(index, prev)]
        #     longest, result = 0, 0
        #     for i in range(index, len(nums)):
        #         if prev < nums[i]:
        #             longest = max(longest, 1 + dfs(i+1, nums[i]))
        #     dp[(index, prev)] = longest
        #     return dp[(index, prev)]
        # return dfs(0, float("-inf"))

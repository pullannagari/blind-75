from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # result = nums[0]
        # for i in range(1, len(nums)+1):
        #     if i < len(nums):
        #         result = result ^ nums[i]
        #     result = result ^ i
        # return result
        n = len(nums)
        target_sum = ((n+1)*(n))//2
        current_sum = sum(nums)
        return target_sum - current_sum
        
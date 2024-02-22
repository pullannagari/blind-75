from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res = max(nums)
        curr_min = 1
        curr_max = 1
        for num in nums:
            tmp = curr_max*num
            curr_max = max(curr_min*num, tmp, num)
            curr_min = min(curr_min*num, tmp, num)
            max_res = max(max_res, curr_max)
        return max_res
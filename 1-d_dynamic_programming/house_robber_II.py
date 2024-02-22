from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def robbing_helper(nums: List[int]):
            max_amount = 0
            prev_max = 0
            for num in nums:
                temp = max(prev_max + num, max_amount)
                prev_max = max_amount
                max_amount = temp
            return max_amount

        return max(robbing_helper(nums[:-1]), robbing_helper(nums[1:]))
             
        
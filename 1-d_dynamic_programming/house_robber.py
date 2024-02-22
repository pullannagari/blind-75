from typing import List

class Solution:

    # we keep track of two maximums
    # one with the max without considering the current element
    # one without considering the current element
    # we keep shifting the max based on both the cases to track the overall max
    def __init__(self):
        self.dp = {}

    def rob(self, nums: List[int]) -> int:
        max_amount = 0
        prev_max = 0
        for num in nums:
            temp = max(prev_max + num, max_amount)
            prev_max = max_amount
            max_amount = temp
        return max_amount



        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) in self.dp:
        #     return self.dp[len(nums)]
        # self.dp[len(nums)] = max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
        # return self.dp[len(nums)]
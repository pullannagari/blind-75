from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        return self.min_helper(left, right, nums)

    def min_helper(self, left, right, nums):
        if left == right:
            return nums[left]
        mid = left + (right-left) // 2
        if nums[left] <= nums[mid]:
            right_res = self.min_helper(mid+1, right, nums)
            if nums[left] < right_res:
                return nums[left]
            else:
                return right_res
        elif nums[right] >= nums[mid]:
            left_res = self.min_helper(left, mid-1, nums)
            if nums[mid] < left_res:
                return nums[mid]
            else:
                return left_res
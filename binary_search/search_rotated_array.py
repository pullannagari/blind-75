from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        return self.search_target(low, high, nums, target)

    def search_target(self, low, high, nums, target):
        if low == high:
            if nums[low] == target:
                return low
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                return self.search_target(low, mid-1, nums, target)
            else:
                return self.search_target(mid+1, high, nums, target)
        else:
            if nums[mid] < target <= nums[high]:
                return self.search_target(mid+1, high, nums, target)
            else:
                return self.search_target(low, mid-1, nums, target)

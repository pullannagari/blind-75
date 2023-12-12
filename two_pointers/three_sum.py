class Solution:
    def threeSum(self, nums: list) -> list:
        result = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and nums[index-1] == nums[index]:
                continue
            left, right = index + 1, len(nums)-1
            while left < right:
                if num + nums[left] + nums[right] > 0:
                    right -= 1
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
        
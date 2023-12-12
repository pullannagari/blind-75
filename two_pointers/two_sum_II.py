class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]
        
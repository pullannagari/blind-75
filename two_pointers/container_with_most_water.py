class Solution:
    def maxArea(self, height: list) -> int:
        max_wat = 0
        left, right = 0, len(height)-1
        while left < right:
            curr_max = min(height[left], height[right]) * (right-left)
            max_wat = max(max_wat, curr_max)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_wat
        
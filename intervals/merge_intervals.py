from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        intervals.sort(key=lambda x:x[0] )
        result = [intervals[0]]
        while i < len(intervals):
            left = result[-1]
            right = intervals[i]
            if left[1] < right[0]:
                result.append(right)
            elif left[0] > right[1]:
                result.pop()
                result.append(right)
                result.append(left)
            else:
                minl = min(left[0], right[0])
                maxr = max(left[1], right[1])
                result[-1][0] = minl
                result[-1][1] = maxr
            i += 1
        return result
        
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start = [intr[0] for intr in intervals]
        end = [intr[1] for intr in intervals]
        start.sort()
        end.sort()
        count = 0
        si, ei = 0, 0
        result = 0
        while si < len(start):
            if start[si] < end[ei]:
                count += 1
                si += 1
            else:
                ei += 1
                count -= 1
            result = max(result, count)
        return result
            


        
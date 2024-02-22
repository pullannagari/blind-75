from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                return False
            else:
                prevEnd = end
        return True
        
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # newintrvl = newInterval
        # result = []
        # for i, intrvl in enumerate(intervals):
        #     if intrvl[0] > newintrvl[1]:
        #         result.append(newintrvl)
        #         result.extend(intervals[i:])
        #         return result
        #     elif intrvl[1] < newintrvl[0]:
        #         result.append(intrvl)
        #     else:
        #         minl = min(intrvl[0], newintrvl[0])
        #         maxr = max(intrvl[1], newintrvl[1])
        #         newintrvl = [minl, maxr]
        # result.append(newintrvl)
        # return result

        new_start, new_end = newInterval
        result = []
        for i, interval in enumerate(intervals):
            start, end = interval
            if new_end < start:
                result.append([new_start, new_end])
                result.extend(intervals[i:])
                return result
            elif new_start > end:
                result.append(interval)
            else:
                new_end = max(new_end, end)
                new_start = min(new_start, start)
                newInterval = [new_start, new_end]
        result.append(newInterval)
        return result
            


        
import heapq

class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        sl = len(self.small_heap)
        ll = len(self.large_heap)
        if sl > ll:
            if -self.small_heap[0] > num:
                l_ele = heapq.heappop(self.small_heap)
                heapq.heappush(self.large_heap, -l_ele)
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heappush(self.large_heap, num)
        elif sl < ll:
            if self.large_heap[0] < num:
                s_ele = heapq.heappop(self.large_heap)
                heapq.heappush(self.small_heap, -s_ele)
                heapq.heappush(self.large_heap, num)
            else:
                heapq.heappush(self.small_heap, -num)
        else:
            if not self.small_heap or -self.small_heap[0] >= num:
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heappush(self.large_heap, num)

        

    def findMedian(self) -> float:
        # print(self.small_heap, self.large_heap)
        sl = len(self.small_heap)
        ll = len(self.large_heap)
        if sl > ll:
            return -self.small_heap[0]
        elif sl < ll:
            return self.large_heap[0]
        else:
            return (self.large_heap[0] + -self.small_heap[0]) / 2
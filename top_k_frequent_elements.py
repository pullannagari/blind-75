from collections import defaultdict

class Solution:
    # O(n) solution, uses O(n) additional space
    def topKFrequent(self, nums: list, k: int) -> list:
      if not nums:
        return None
      freq_map = defaultdict(int)
      for num in nums:
        freq_map[num] += 1
      freq_bucket = [-1]*(len(nums)+1) # initialize the bucket with values as len+1
      for key in freq_map:
        index = freq_map[key]
        if freq_bucket[index] == -1:
          freq_bucket[index] = [key]
        else:
          freq_bucket[index].append(key)
      curr_index = len(nums)
      result = []
      print(freq_bucket)
      while k > 0:
        if freq_bucket[curr_index] != -1:
          k -= len(freq_bucket[curr_index])
          result.extend(freq_bucket[curr_index])
        curr_index -= 1
      return result

      # O(nlogn) solution, we can come up with a better solution
      # if not nums:
      #   return None
      # freq_map = defaultdict(int)
      # for num in nums:
      #   freq_map[num] += 1
      # mheap = []
      # for key in freq_map:
      #   heapq.heappush(mheap,(-freq_map[key], key))
      # result = []
      # for i in range(k):
      #   result.append(heapq.heappop(mheap)[1])
      # return result

        
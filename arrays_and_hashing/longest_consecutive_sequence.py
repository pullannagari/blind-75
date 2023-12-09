class Solution:
    def longestConsecutive(self, nums: list) -> int:
        numset = set(nums)
        unique_nums = list(numset)
        longest = 0
        for n in unique_nums:
            if n-1 not in numset:
                new_longest = 1
                # don't change n since we need to iterate over each element
                # just use the result directly for checking the condition instead
                while n+new_longest in numset:
                    new_longest += 1
                longest = max(new_longest, longest)
        return longest
        
        # i = 0
        # while i < len(unique_nums):
        #     n = unique_nums[i]
        #     new_longest = 0
        #     while n in numset:
        #         new_longest += 1
        #         n += 1
        #         i += 1
        #     longest = max(longest, new_longest)
        # return longest
                
                
                
        
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        if not nums:
            return False
        distinct = set()
        for num in nums:
            if num in distinct:
                return True
            else:
                distinct.add(num)
        return False
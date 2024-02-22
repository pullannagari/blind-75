class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        # bottom-up
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(1, n-1):
            res = a + b
            a = b
            b = res
        return res

        
        
        # top-down memoization
        # if n in self.memo:
        #     return self.memo[n]
        # if n <= 2:
        #     return n
        # self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        # return self.memo[n]
        
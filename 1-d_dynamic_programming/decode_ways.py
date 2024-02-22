class Solution:

    # the pattern here is, when we want to calculate ways
    # we come up with an array of size n + 1
    # and then we go from back to front, 
    # conditionally incrementing/decrementing the ways
    # we also need to ensure that we reuse the calculations made so far

    def numDecodings(self, s: str) -> int:
        dp = []
        def dfs(index):
            if index in dp:
                return dp[index]
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            result = dfs(index+1)
            if index+1 < len(s) and (s[index] == "1" or (
                s[index] == "2" and s[index+1] in "0123456")):
                result += dfs(index+2)
            dp[index] = result
            return dp[index]
        #return dfs(0)

        # bottom-up
        dp = [0]*(len(s)+1)
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            print(dp)
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i+1 < len(s) and (s[i] == "1" or (
                s[i] == "2" and s[i+1] in "0123456"
            )):
                dp[i] += dp[i+2]
        return dp[0]
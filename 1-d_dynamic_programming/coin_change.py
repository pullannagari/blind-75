from typing import List

class Solution:
    # when we need the min coins, we need tabulation with the length of 
    # the amount+1 with 0th col set to 0 and then go left to right 
    # calculating the min coins for each amount, based on each coin

    def coinChange(self, coins: List[int], amount: int) -> int:
        # using bottom up tabulation
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        if dp[amount] == amount+1:
            return -1
        return dp[amount]


        # using top-down dp
        # dp = {}
        # def dfs(amount):
        #     if amount in dp:
        #         return dp[amount]
            
        #     # case where the result is not possible
        #     if amount < 0:
        #         return -1

        #     # case where the coin combination results in target amount
        #     if amount == 0:
        #         return 0

        #     # sys.maxsize gives the integer maximum in python
        #     min_val = sys.maxsize
        #     for coin in coins:
        #         res = dfs(amount-coin)
        #         if res != -1:
        #             # add 1 for considering this coin to the result target
        #             min_val = min(min_val, res+1)
        #     dp[amount] = min_val
        #     return dp[amount]

        # result = dfs(amount)

        # if result == sys.maxsize:
        #     return -1

        # return result
                    



            

            
            
        

        
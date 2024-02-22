from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up tabulation
        tab = [False]*(len(s)+1)
        tab[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(word)+i <= len(s):
                    if s[i:len(word)+i] == word:
                        tab[i] = tab[i+len(word)]
                if tab[i]:
                    break
        return tab[i]


        # top-down dynamic programming
        dp = {}
        def dfs(index):
            if index in dp:
                return dp[index]
            if index == len(s):
                return True
            found = False
            for word in wordDict:
                endindex = index + len(word)
                if endindex <= len(s):
                    if word == s[index:endindex]:
                        if dfs(endindex):
                            found = True
                            break
            dp[index] = found
            return dp[index]
        # return dfs(0)

        
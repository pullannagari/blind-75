from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index, curr_res, tar_rem):
            if tar_rem == 0:
                result.append(curr_res.copy())
                return
            if index >= len(candidates):
                return
            if tar_rem <= 1:
                return
            curr_res.append(candidates[index])
            dfs(index, curr_res, tar_rem - candidates[index])
            curr_res.pop()
            dfs(index+1, curr_res, tar_rem)
        dfs(0, [], target)    
        return result
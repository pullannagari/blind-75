from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = {c:[] for word in words for c in word}
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            else:
                for j in range(min_len):
                    if word1[j] != word2[j]:
                        adj_list[word1[j]].append(word2[j])
                        break
        # set to track if the node has already been visited, 
        # we shouldn't add it to the result
        visited = set()
        # set to track if the node is already in the path and 
        # we are visiting again, ambiguous - so we return ""
        path = set()
        result = []
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for child in adj_list[node]:
                if not dfs(child):
                    return False
            path.remove(node)
            visited.add(node)
            # post oreder dfs, since we are 
            # adding the node after we have visited the node
            result.append(node)
            return True
        for c in adj_list:
            if not dfs(c):
                return ""
        result = "".join(result)
        return result[::-1]
            
            


        
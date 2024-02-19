from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # using the union/find operation or segment tree

        # initializing the each node's parent as it's own
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            par_n1 = find(n1)
            par_n2 = find(n2)
            if par_n1 == par_n2:
                return 0
            if rank[par_n1] >= rank[par_n2]:
                parent[par_n2] = par_n1
                rank[par_n1] += 1
            else:
                parent[par_n1] = par_n2
                rank[par_n2] += 1
            return 1
        result = n
        for edge in edges:
            result -= union(edge[0], edge[1])
        return result

        
        
        # def using_visited():
        #     # nodes/vertices
        #     adj_list = {nde:[] for nde in range(n)}
        #     # adjacency list
        #     for edge in edges:
        #         frm, to = tuple(edge)
        #         adj_list[frm].append(to)
        #         adj_list[to].append(frm)
        #     def dfs(node):
        #         if node in visited:
        #             return False
        #         visited.add(node)
        #         for con_node in adj_list[node]:
        #             dfs(con_node)
        #         return True
        #     visited = set()
        #     result = 0
        #     for nde in range(n):
        #         if nde not in visited:
        #             if dfs(nde):
        #                 result += 1
        #     return result
        # return using_visited()
        
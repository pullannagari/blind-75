from typing import List

class Solution:
    def __init__(self):
        self.components = None

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # using dfs and prev node concept
        # nodes = {i:[] for i in range(n)}
        # for edge in edges:
        #     frm, to = tuple(edge)
        #     nodes[to].append(frm)
        #     nodes[frm].append(to)
        # visited = set()
        # def dfs(node, prev):
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for child in nodes[node]:
        #         if child != prev:
        #             if not dfs(child, node):
        #                 return False
        #     return True
        # if not dfs(0,-1):
        #     return False
        # return len(visited) == n

        # using union find to detect a cycle
        # if there is a cycle its not a valid tree
        parent = [i for i in range(n)]
        rank = [1]*n
        self.components = n
        def find(node):
            while node != parent[node]:
                node = parent[parent[node]]
            return node

        def union(n1, n2):
            par_n1 = find(n1)
            par_n2 = find(n2)
            if par_n1 == par_n2:
                return False
            else:
                if rank[par_n1] >= rank[par_n2]:
                    parent[par_n2] = par_n1
                    rank[par_n1] += 1
                else:
                    parent[par_n1] = par_n2
                    rank[par_n2] += 1
                self.components -= 1 
                return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return False
        return self.components == 1
                
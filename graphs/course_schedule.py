from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = dict()
        for nde in range(numCourses):
            adjList[nde] = []
        for fr, to in prerequisites:
            adjList[fr].append(to)
        def dfs(node):
            if node in visitedSet:
                return False
            if adjList[node] == []:
                return True
            visitedSet.add(node)
            for dep_node in adjList[node]:
                if not dfs(dep_node):
                    return False
            visitedSet.remove(node)
            adjList[node] = []
            return True
        for crs in range(numCourses):
            visitedSet = set()
            if not dfs(crs):
                return False
        return True
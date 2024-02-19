
from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            cpy = Node(node.val)
            old_to_new[node] = cpy
            for neighbor in node.neighbors:
                cpy.neighbors.append(dfs(neighbor))
            return cpy

        def bfs():
            if not node:
                return node
            if not node.neighbors:
                return Node(node.val)
            new_nodes = {}
            visited = set()
            queue = deque()
            queue.append(node)
            ret_node = Node(node.val)
            new_nodes[ret_node.val] = ret_node
            while queue:
                curr_node = queue.popleft()
                if curr_node.val not in visited:
                    if curr_node.val not in new_nodes:
                        new_node = Node(curr_node.val)
                    else:
                        new_node = new_nodes[curr_node.val]
                    for neighbor in curr_node.neighbors:
                        if neighbor.val in new_nodes:
                            new_node.neighbors.append(new_nodes[neighbor.val])
                        else:
                            neighbor_node = Node(neighbor.val)
                            new_nodes[neighbor.val] = neighbor_node
                            new_node.neighbors.append(neighbor_node)
                        queue.append(neighbor)
                        visited.add(curr_node.val)
            return ret_node
        return dfs(node)
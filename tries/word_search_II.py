from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.children = {}

    def search(self, word) -> bool:
        curr = self.root
        for i, ch in enumerate(word):
            if ch in curr.children:
                curr = curr.children[ch]
                if len(word)-1 == i:
                    if curr.is_word:
                        return True
                    return False
            else:
                return False

    def search_prefix(self, word) -> bool:
        curr = self.root
        for i, ch in enumerate(word):
            if ch in curr.children:
                curr = curr.children[ch]
                if len(word)-1 == i:
                    return True
            else:
                return False
        

    def insert(self, word):
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.insert(word)
        result = set()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def dfs(row, col, prefix, node):
            if row < 0 or col < 0:
                return
            if row >= len(board) or col >= len(board[0]):
                return
            if visited[row][col]:
                return
            if board[row][col] not in node.children:
                return
            visited[row][col] = True
            node =  node.children[board[row][col]]
            prefix += board[row][col]
            if node.is_word:
                result.add(prefix)
            dfs(row+1, col, prefix, node)
            dfs(row-1, col, prefix, node)
            dfs(row, col+1, prefix, node)
            dfs(row, col-1, prefix, node)
            visited[row][col] = False

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, "", t.root)
        return list(result)
from typing import List

class Solution:
    def __init__(self):
        self.found = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if row >= len(board) or col >= len(board[0]):
                return
            if row < 0 or col < 0:
                return
            if i >= len(word):
                return
            if visited[row][col]:
                return
            visited[row][col] = True
            if board[row][col] == word[i]:
                if i == len(word)-1:
                    self.found = True
                    return
                i += 1
                dfs(row+1, col, i)
                dfs(row-1, col, i)
                dfs(row, col+1, i)
                dfs(row, col-1, i)
            visited[row][col] = False

        visited = [ [False for _ in range(len(board[0]))] for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    print(board[row][col])
                    dfs(row, col, 0)
                    if self.found:
                        return True
        return False
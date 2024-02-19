# class TrieNode:
#     def __init__(self, ch=None):
#         self.val = ch
#         self.next = []
#         self.is_word = False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if i == len(word)-1:
                curr.is_word = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for i, ch in enumerate(word):
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
            if i == len(word)-1:
                if curr.is_word:
                    return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, ch in enumerate(prefix):
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
            if i == len(prefix)-1:
                return True
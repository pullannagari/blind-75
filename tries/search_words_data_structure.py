class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i, ch in enumerate(word):
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if i == len(word)-1:
                curr.is_word = True
        

    def search(self, word: str) -> bool:
        def check_char_match(curr, index):
            if index == len(word):
                if curr.is_word:
                    return True
                return False
            if word[index] == ".":
                for child in curr.children:
                    if check_char_match(curr.children[child], index+1):
                        return True
                return False
            elif word[index] in curr.children:
                curr = curr.children[word[index]]
                return check_char_match(curr, index+1)
            else:
                return False

        return check_char_match(self.root, 0)
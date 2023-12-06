class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for ch in s:
            if ch in char_map:
                char_map[ch] += 1
            else:
                char_map[ch] = 1
        for ch in t:
            if ch in char_map:
                if char_map[ch] == 1:
                    del char_map[ch]
                else:
                    char_map[ch] -= 1
            else:
                return False
        if not char_map:
            return True
        return False

        
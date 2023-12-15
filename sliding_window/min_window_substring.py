from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left = 0
        right = 0
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        for ch in t:
            t_dict[ch] += 1
        for ch in t_dict:
            s_dict[ch] = 0
        have = 0
        need = len(t_dict.keys())
        result = ""
        while left <= right and right < len(s):
            while have < need and right < len(s):
                if s[right] in s_dict:
                    s_dict[s[right]] += 1
                    if s_dict[s[right]] == t_dict[s[right]]:
                        have += 1
                right += 1
            if have == need:
                if result == "" or (right-left) < len(result):
                        result = s[left:right]
            while have == need and left <= right:
                if s[left] in s_dict:
                    s_dict[s[left]] -= 1
                    if s_dict[s[left]] < t_dict[s[left]]:
                        have -= 1
                if (right-left) < len(result):
                    result = s[left:right]
                left += 1
        return result
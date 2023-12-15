class Solution:
    def isValid(self, s: str) -> bool:
        # LIFO
        stack = []
        paren_map = {']':'[','}':'{',')':'('}
        for ch in s:
            if ch in paren_map.values():
                stack.append(ch)
            elif stack:
                if ch in paren_map:
                    if stack[-1] == paren_map[ch]:
                        del stack[-1]
                    else:
                        return False
            else:
                return False
        return len(stack) == 0


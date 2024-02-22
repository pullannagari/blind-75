class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def get_palindrome(l, r):
            palindrome = ""
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    palindrome = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            return palindrome

        result = ""

        for i in range(0, len(s)-1):
            el, er, oddl, oddr = 0, 0, 0, 0
            epalindrome = ""
            # even case
            if s[i] == s[i+1]:
                el = i
                er = i + 1
                epalindrome = get_palindrome(el, er)
            # odd case
            opalindrome = get_palindrome(oddl, oddr)
            palindrome = epalindrome if len(epalindrome) > len(opalindrome) else opalindrome
            if len(result) < len(palindrome):
                result = palindrome
        return result
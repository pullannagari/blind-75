class Solution:
    def isPalindrome(self, s: str) -> bool:
        # not using extra memory
        l = 0
        h = len(s)-1
        while l < h:
            while l < h and not self.is_alpha_num(s[l]):
                l += 1
            while l < h and not self.is_alpha_num(s[h]):
                h -= 1
            if s[l].lower() != s[h].lower():
                return False
            l += 1
            h -= 1
        return True

    
    def is_alpha_num(self, ch):
        if (ord('A') <= ord(ch) <= ord('Z') or
            ord('a') <= ord(ch) <= ord('z') or
            ord('0') <= ord(ch) <= ord('9')):
            return True
        return False


        # using extra memory
        # ts = []
        # for ch in list(s):
        #     if ch.isalnum():
        #         if ch.isupper():
        #             ch = ch.lower()
        #         ts.append(ch)
        # ts = "".join(ts)
        # mid = len(ts)//2
        # l = mid - 1
        # if len(ts)%2 == 0:
        #     r = mid
        # elif len(ts)%2 != 0:
        #     r = mid + 1
        # while l >= 0 and r <= len(ts)-1:
        #     if ts[l] != ts[r]:
        #         return False
        #     l -= 1
        #     r += 1
        # return True



        
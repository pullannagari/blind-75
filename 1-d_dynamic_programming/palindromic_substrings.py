class Solution:
    def countSubstrings(self, s: str) -> int:
        # bruteforce
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         sub_s = s[i:j+1]
        #         if sub_s:
        #             if sub_s == sub_s[::-1]:
        #                 count += 1
        # return count

        # idea is that instead of getting all the substrings and then determining them if they are palidrome
        # we calculate all the possible palidromes for the given string taking each char as mid of palidrome
        
        # start at each character and assume it as the center of the palindrome substring
        # then expand outwards to count the matching characters
        # we repeat this once for odd and once for even set of characters
        def get_palindrome_count(left, right):
            count = 0
            while left > -1 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
            return count

        result = 0
        for i in range(len(s)):
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    result += get_palindrome_count(i, i+1)
            result += get_palindrome_count(i, i)
        return result

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        alpha_dict = defaultdict(int)
        res = 0
        while left <= right and right < len(s):
            alpha_dict[s[right]] += 1
            size = right - left + 1
            maxf = 0
            for ch in alpha_dict:
                maxf = max(maxf, alpha_dict[ch])
            if size - maxf <= k:
                res = max(res, size)
            else:
                while size - maxf > k:
                    alpha_dict[s[left]] -= 1
                    maxf = 0
                    for ch in alpha_dict:
                        maxf = max(maxf, alpha_dict[ch])
                    left += 1
                    size -= 1
            right += 1
        return res
                



        # doesn't work for the cases of shifting left pointer
        # i = 0
        # j = 0
        # curr_k = k
        # curr_ch = ""
        # max_len = 0
        # curr_count = 0
        # while j < len(s) and i <= j:
        #     if curr_ch == "":
        #         curr_ch = s[j]
        #         curr_count += 1
        #         max_len = max(max_len, curr_count)
        #         j += 1
        #     elif curr_ch == s[j] or curr_k != 0:
        #         if curr_ch != s[j]:
        #             curr_k -= 1
        #         curr_count += 1
        #         max_len = max(max_len, curr_count)
        #         j += 1
        #     else:
        #         while s[i] != s[j]:
        #             i += 1
        #         curr_k = k
        #         curr_count = 0
        #         curr_ch = s[i]
        #         while i < j:
        #             if s[i] == curr_ch or curr_k != 0:
        #                 if s[i] != curr_ch:
        #                     curr_k -= 1
        #                 curr_count += 1
        #                 max_len = max(max_len, curr_count)
        #             i += 1
        # return max_len
        
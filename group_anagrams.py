from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        srt_map = defaultdict(list)
        for s in strs:
            ch_counter = [0]*26
            for ch in s:
                ch_counter[ord(ch)-ord('a')] += 1
            srt_map[tuple(ch_counter)].append(s)
        return srt_map.values()
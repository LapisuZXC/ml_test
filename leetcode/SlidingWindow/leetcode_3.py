"""
Given a string s, find the length of the longest
substring
without repeating characters.
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                seen.remove(s[l])
                l += 1

        return longest


s = Solution()
print(s.lengthOfLongestSubstring("abcdacvvsca"))

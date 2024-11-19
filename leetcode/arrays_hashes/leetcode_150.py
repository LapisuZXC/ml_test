"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""

from typing import List
import re


class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        l_arr = [len(string) for string in strs]

        for i in range(len(strs)):
            result += str(l_arr[i]) + "#" + strs[i]
        return result

    def decode(self, s: str) -> List[str]:
        l = re.split(r"\d+#", s)
        return l[1:]


example = ["we", "love", "code"]
s = Solution()
e = s.encode(example)
d = s.decode(e)
print(e, d)

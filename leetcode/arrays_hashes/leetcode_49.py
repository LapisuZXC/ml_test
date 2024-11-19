"""
Given an array of strings strs, group the
anagrams
together. You can return the answer in any order.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            l = "".join(sorted(i))
            if l not in d.keys():
                d[l] = [
                    i,
                ]
            else:
                d[l].append(i)

        return [x for x in d.values()]

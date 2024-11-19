"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        arr = list(set(nums))
        arr.sort()
        result = 1
        best_result = 1

        for i in range(len(arr)):
            if arr[i] == (arr[i - 1] + 1):
                result += 1
            else:
                result = 1
            if result > best_result:
                best_result = result
        return best_result

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        pre = 1
        post = 1

        for i in range(l):
            res[i] = pre
            pre *= nums[i]

        for i in range((l - 1), -1, -1):
            res[i] *= post
            post *= nums[i]

        return res

from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in combinations(nums, 3):
            if sum(i) == 0:
                result.add(i)
        return list(result)


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()

print(s.threeSum(nums))

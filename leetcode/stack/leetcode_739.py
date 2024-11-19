from typing import List

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                a = 0
                if temperatures[j] > temperatures[i]:
                    a = j - i
                    break
            stack.append(a)
        return stack


s = Solution()

case1 = [73, 74, 75, 71, 69, 72, 76, 73]
case2 = [30, 40, 50, 60]
print(s.dailyTemperatures(case1))
print(s.dailyTemperatures(case2))

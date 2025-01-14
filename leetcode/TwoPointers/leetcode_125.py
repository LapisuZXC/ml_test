class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while not s[left].isalnum() or s[left] == " ":
                left += 1
            while not s[right].isalnum() or s[right] == " ":
                right += 1
            if s[left] != s[right]:
                return False
            if left >= right:
                break
            left += 1
            right -= 1
        return True

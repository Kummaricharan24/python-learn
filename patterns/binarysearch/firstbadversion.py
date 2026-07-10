class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:          # note: strict <, not <=
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid           # mid could still be the answer, keep it in range
            else:
                left = mid + 1
        return left
s1=Solution
print(s1.firstBadVersion(5,4))
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(1 for h, e in zip(heights, expected) if h != e)
s1=Solution()
print(s1.heightChecker([1,1,4,2,1,3]))
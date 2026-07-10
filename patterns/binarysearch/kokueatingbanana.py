class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(speed):
            return sum(math.ceil(pile/speed)for pile in piles)
        left=1
        right=max(piles)
        while left<right:
            mid=left+(right-left)//2
            if hours_needed(mid)<=h:
                right=mid
            else:
                left=mid+1
        return left

s1=Solution()
print(s1.minEatingSpeed( [3,6,7,11], 8))
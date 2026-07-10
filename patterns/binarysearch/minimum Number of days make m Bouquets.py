class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def can_make(days):
            bouquets=0
            flowers=0
            for bloom in bloomDay:
                if bloom <=days:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                        flowers=0
            return bouquets>=m
        left=min(bloomDay)
        right=max(bloomDay)
        while left<right:
            mid=(left+right)//2
            if can_make(mid):
                right=mid
            else:
                left=mid+1
        return left
s1=Solution()
print(s1.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
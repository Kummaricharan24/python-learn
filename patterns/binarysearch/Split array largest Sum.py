class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(mid):
            count=1
            current_sum=0
            for num in nums:
                if current_sum + num > mid:
                    count+=1
                    current_sum=num
                else:
                    current_sum+=num
            return count<=k
        low=max(nums)
        high=sum(nums)
        while low<high:
            mid=(low+high)//2
            if canSplit(mid):
                high=mid
            else:
                low=mid+1
        return low


s1=Solution()
print(s1.splitArray(nums = [7,2,5,10,8], k = 2))
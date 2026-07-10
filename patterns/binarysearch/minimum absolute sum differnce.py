class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD=10**9+7
        n=len(nums1)
        sorted_nums=sorted(nums1)
        max_gain=0
        total_diff=0
        for i in range(n):
            diff=abs(nums1[i]-nums2[i])
            total_diff+=diff
            
            if diff==0:
                continue
            pos = bisect.bisect_left(sorted_nums, nums2[i])
            if pos<n:
                new_diff=abs(sorted_nums[pos]-nums2[i])
                max_gain=max(max_gain,diff-new_diff)
            if pos>0:
                new_diff=abs(sorted_nums[pos-1]-nums2[i])
                max_gain=max(max_gain,diff-new_diff)
        return (total_diff-max_gain)%MOD
s1=Solution()
print(s1.minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5]))
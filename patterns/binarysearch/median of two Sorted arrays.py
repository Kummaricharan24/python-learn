class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        half=(m+n+1)//2
        low=0
        high=m
        while low<=high:
            i=(low+high)//2
            j=half-i
            left1=nums1[i-1]if i>0 else float('-inf')
            right1=nums1[i]if i<m else float('inf')
            left2=nums2[j-1]if j>0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')      
            if left1<=right2 and left2<=right1:
                if(m+n)%2==0:
                    return (max(left1,left2)+min(right1,right2))/2
                else :
                    return max(left1,left2)
            elif left1>right2:
                high =i-1
            else:
                low=i+1
        return -1
                    
s1=Solution()
print(s1.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
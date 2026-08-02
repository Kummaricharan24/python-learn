class Solution(object):
    def longestOnes(self, nums, k):
        best=0
        left=0
        zeros=0
        for right,val in enumerate(nums):
            if val==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            best=max(best,right-left+1)
        return best
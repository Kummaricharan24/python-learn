class Solution:
    def removeDuplicates(self,num):
        left=0
        right=1

        while right<len(num):
            if num[left]!=num[right]:
                left+=1
            
                num[left]=num[right]
            right+=1
        for i in range(left+1,len(num)):
            num[i]='-'
        return left+1

s1=Solution()
num=[1,1,2]
print(s1.removeDuplicates(num))
print(num)
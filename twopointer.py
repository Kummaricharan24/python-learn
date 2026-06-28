#two pointer first problem
num=[2,7,9,11,15]
def Twopointer(num,target):
    left =0 
    right=len(num)-1
    while left<right:
        target=11
        sum_current=num[left]+num[right]
        
        if sum_current==target:
            return [left ,right]
        elif sum_current>target:
            right-=1
        else:
            left+=1
    return
print(Twopointer(num,9))#op:[0, 2]


#secound problem dubilicate
a=input().split(",")
h=[int(c) for c in a]
def Duplicate(num):
    
    newl=[]
    for i in num:
        if i not in newl:
            
            newl.append(i)
    
    return newl
    s=set(num)
    newl=list(s)
    newl.sort()
    return newl


print(Duplicate(h)) #op:[1, 2]

   

def remove_duplicates(input_list):
    seen = set()
    output = []
    
    for num in input_list:
        if num not in seen:
            seen.add(num)
            output.append(num)
        else:
            output.append('_')
    
    return output

# Run
input_list = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
output = remove_duplicates(input_list)
print(output)
# Output: [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']



def remove_duplicates(input_list):
    n = len(input_list)
    output = input_list.copy()  # Copy input to output
    
    left = 0  # Points to unique elements
    right = 1  # Scans ahead for duplicates
    
    while right < n:
        is_duplicate = False # Assume NOT duplicate at start
        
        # Check if output[right] already exists between 0 and right-1
        for i in range(right):
            if output[i] == output[right]:
                is_duplicate = True ## Found duplicate → switch to True
                break
        
        if is_duplicate:
            output[right] = '_'  # Mark duplicate as '_'
        else:
            left = right         # Move left to new unique position
        
        right += 1               # Always move right forward
    
    return output

# Run
input_list = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
output = remove_duplicates(input_list)
print(output)
# Output: [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
print(remove_duplicates([0, 1, 2, 3, 4, 2, 2, 3, 3, 4]))
#op:[0, 1, 2, 3, 4, '_', '_', '_', '_', '_']


#palindrome 
stri="A man, a plan, a canal: Panama"
cleaned = ''.join(ch.lower() for ch in stri if ch.isalnum())
print(cleaned)



def Palindrome(cleaned):
    left=0
    right=len(cleaned)-1
    while left<right:
        if cleaned[left]!=cleaned[right]:
            return False
        left+=1
        right-=1    
    return True
print(Palindrome(cleaned))
op:amanaplanacanalpanama
True
#container with most water
height=[1,8,6,2,5,4,8,3,7]
def heightwater(height):
    left=0
    right=len(height)-1
    max_area=0
    while left<right:
        area=min(height[left],height[right])*(right-left)
        max_area=max(max_area,area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_area
print(heightwater(height))#op:49


def move_zeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))           
#op:
[1, 3, 12, 0, 0]
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


s1 = Solution()
s = ["h", "e", "l", "l", "o"]

print(s1.reverseString(s))



class Solution:
    def duplicate(self,num):
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
num=[0,0,1,1,2,2,3]
print(s1.duplicate(num))
print(num)
#op:4
[0, 1, 2, 3, '-', '-', '-']



class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        currrent_sum=0
        while left<right:
            current_sum=numbers[left]+numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            if current_sum<target:
                left+=1
            else:
                right-=1
        return currrent_sum
s1=Solution()
result=s1.twoSum([2,7,11,15],9)
print(result)#op:[1, 2]

            
#moveZero 
class Solution():
    def moveZeroes(self, nums):
        left=0
        
        for i in range (len(nums)):
            if nums[i]!=0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
        return nums
            
s1 = Solution()
result = s1.moveZeroes([0, 1, 0, 3, 12])
print(result)  # [1, 3, 12, 0, 0]


#reverse string
class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s

s1=Solution()
result=s1.reverseString(["h","e","l","l","o"])
print(result)#op:['o', 'l', 'l', 'e', 'h']


class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
s1=Solution()
result=s1.maxArea([1,8,6,2,5,4,8,3,7,9])
print(result)#op:64

#valid palindrome
class Solution(object):
    def isPalindrome(self, s):
        cleaned="".join(i.lower()  for i in s if i.isalnum())
        left=0
        right=len(cleaned)-1
        while left<right:
            if cleaned[left]!=cleaned[right]:
                return False
            left+=1
            right-=1
        return True
        
s1=Solution()
result=s1.isPalindrome("A man, a plan, a canal: Panama")
print(result)#op:True
s2=Solution()
result=s2.isPalindrome("charan")
print(result)#op:False

#https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution(object):
    def sortedSquares(self, nums):
        
        left=0
        right=len(nums)-1
        result=[0]*len(nums) ## [0, 0, 0, 0, 0]
        pos=len(nums)-1      # Largest square always goes LAST
                             #→ so we fill result back to front
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]**2
                left+=1
            else:
                result[pos]=nums[right]**2
                right-=1
            pos -=1
        return result

s1 = Solution()
result = s1.sortedSquares([-20, -1, 0, 3, 10])
print(result)  # [0, 1, 9, 16, 100]

#sub array product less then k
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k<=1:
            return 0
        product=1
        count=0
        left=0
            
        for i in range(len(nums)):
            product*=nums[i]
            while product>=k:
                product//=nums[left]
                left+=1
            count+=i-left+1
        return count
s1 = Solution()
result = s1.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
print(result) #op:8


#remove element 
class Solution(object):
    def removeElement(self, nums, val):
        left=0
        

        
        for right in range(len(nums)):
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1
        return left

                
s1 = Solution()
result = s1.removeElement([3, 2, 2, 3], 3)
print(result) #op:2


#3 sum
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:#skip duplicates
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:#skip duplication
                        left+=1
                    while left<right and nums[right]==nums[right-1]:#skip duplication
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return result


s1=Solution()
result=s1.threeSum([-1, 0, 1, 2, -1, -4])
print(result)
        
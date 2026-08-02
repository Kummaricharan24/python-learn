
from typing import List

#using a dictionary to store the numbers we have seen so far and their indices, we can check if the complement of the current number (i.e., target - num) exists in the dictionary. If it does, we return the indices of the two numbers. If not, we add the current number and its index to the dictionary and continue iterating through the list.    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
        return []

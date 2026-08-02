import heapq
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        curr_max=float("-inf")
        for i , num in enumerate(nums):
            heap.append((num[0],i,0))
            curr_max=max(curr_max,num[0])
        heapq.heapify(heap)

        best_range = [float('-inf'), float('inf')]
        while heap:
            curr_min,list_idx,ele_idx=heapq.heappop(heap)
            if curr_max - curr_min < best_range[1]-best_range[0]:
                best_range = [curr_min, curr_max]   
            if ele_idx+1==len(nums[list_idx]):
                break
            next_value=nums[list_idx][ele_idx+1]
            heapq.heappush(heap, (next_value, list_idx, ele_idx + 1))
            curr_max = max(curr_max, next_value)

        return best_range


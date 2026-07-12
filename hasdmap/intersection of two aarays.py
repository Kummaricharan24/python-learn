class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        seen = {}
        for num in nums1:
            seen[num] = seen.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if num in seen and seen[num] > 0:
                result.append(num)
                seen[num] = 0  # avoid adding the same number twice
        
        return result
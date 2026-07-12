class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged = sorted(nums1[:m] + nums2[:n])
        nums1[:] = merged

s1 = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
s1.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)   # nums1 itself got modified in place
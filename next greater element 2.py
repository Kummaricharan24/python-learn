class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []                              # monotonic decreasing stack (values)

        for i in range(2 * n - 1, -1, -1):     # two passes via index doubling
            while stack and stack[-1] <= nums[i % n]:  # pop non-strictly-greater
                stack.pop()

            if i < n and stack:                 # only record during first logical pass
                res[i] = stack[-1]

            stack.append(nums[i % n])           # push current value (both passes)

        return res
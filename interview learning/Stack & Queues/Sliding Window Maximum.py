from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        num = deque()   # will hold indices
        result = []

        for i in range(len(nums)):
            # pop from left if that index is out of the window
            while num and num[0] <= i - k:
                num.popleft()
            while num and nums[num[-1]] <= nums[i]:
                num.pop()

            # add current index from the right
            num.append(i)
            if i >=k-1:
                result.append(nums[num[0]])

            # once window has k elements, gather values and take max
        return result 
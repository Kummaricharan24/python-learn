#maximumSubarraySum
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        seen = {}
        max_sum = 0
        window_sum = 0
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            seen[nums[right]] = seen.get(nums[right], 0) + 1

            if right - left + 1 > k:
                window_sum -= nums[left]
                seen[nums[left]] -= 1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left += 1

            if right - left + 1 == k and len(seen) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum


# --- Test code ---
sol = Solution()
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
result = sol.maximumSubarraySum(nums, k)
print(result)   # should print 15





#lengthOfLongestSubstring


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# Driver Code
obj = Solution()

print(obj.lengthOfLongestSubstring("abcabcbb"))  # 3
print(obj.lengthOfLongestSubstring("bbbbb"))     # 1
print(obj.lengthOfLongestSubstring("pwwkew"))    # 3
print(obj.lengthOfLongestSubstring(""))          # 0
print(obj.lengthOfLongestSubstring("au"))        # 2



#findMaxAverage




class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = 0
        left = 0
        max_avg = float('-inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            if right - left + 1 > k:
                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_avg = max(max_avg, window_sum / float(k))

        return max_avg


# Driver Code
obj = Solution()

print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(obj.findMaxAverage([5], 1))                     # 5.0
print(obj.findMaxAverage([-1], 1))                    # -1.0


#minSubArrayLen

class Solution(object):
    def minSubArrayLen(self, target, nums):
        window_sum = 0
        min_len = float('inf')
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0


# Driver Code
obj = Solution()

print(obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))     # 2
print(obj.minSubArrayLen(4, [1, 4, 4]))              # 1
print(obj.minSubArrayLen(11, [1, 1, 1, 1, 1, 1]))    # 0
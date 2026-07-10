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


#longestOnes
class Solution(object):
    def longestOnes(self, nums, k):
        best = 0
        left = 0
        zeros = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2



sol = Solution()
print(sol.longestOnes(nums, k))





#longestSubarray
class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        best = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > 1:      # At most one zero in the window
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left)   # Delete one element

        return best


# Test Code
nums = [1, 1, 0, 1]

sol = Solution()
answer = sol.longestSubarray(nums)

print("Output:", answer)



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


# Test Case
s = "abcabcbb"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))


#minWindow

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        have = 0
        window = {}
        required = len(need)

        best_len = float("inf")
        best_left = 0
        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return "" if best_len == float("inf") else s[best_left:best_left + best_len]


# Test Code
s = "ADOBECODEBANC"
t = "ABC"

sol = Solution()
print(sol.minWindow(s, t))





#checkInclusion
from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        left = 0
        window = {}

        for right, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1

            window_size = right - left + 1

            if window_size > len(s1):
                left_char = s2[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            if (right - left + 1) == len(s1) and window == need:
                return True

        return False


# Test Cases
sol = Solution()

print(sol.checkInclusion("ab", "eidbaooo"))      # True
print(sol.checkInclusion("ab", "eidboaoo"))      # False
print(sol.checkInclusion("adc", "dcda"))         # True


#findAnagrams


from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        if not s or not p:
            return []

        window = {}
        need = Counter(p)
        left = 0
        result = []

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            window_size = right - left + 1

            if window_size > len(p):
                left_char = s[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            if right - left + 1 == len(p) and window == need:
                result.append(left)

        return result


# -------------------------
# Test Cases
# -------------------------
sol = Solution()

print(sol.findAnagrams("cbaebabacd", "abc"))   # [0, 6]
print(sol.findAnagrams("abab", "ab"))          # [0, 1, 2]
print(sol.findAnagrams("baa", "aa"))           # [1]




#characterReplacement
class Solution(object):
    def characterReplacement(self, s, k):
        window = {}
        left = 0
        best = 0
        max_freq = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            max_freq = max(max_freq, window[char])

            window_size = right - left + 1

            if window_size - max_freq > k:
                left_char = s[left]
                window[left_char] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


# -------------------------
# Test Cases
# -------------------------
sol = Solution()

print(sol.characterReplacement("ABAB", 2))      # 4
print(sol.characterReplacement("AABABBA", 1))   # 4
print(sol.characterReplacement("AAAA", 2))      # 4
print(sol.characterReplacement("ABCDE", 1))     # 2







#maxSatisfied
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)

        # Customers already satisfied
        baseline = 0
        for i in range(n):
            if grumpy[i] == 0:
                baseline += customers[i]

        # Sliding window
        extra_saved = 0
        best_extra = 0
        left = 0

        for right in range(n):
            if grumpy[right] == 1:
                extra_saved += customers[right]

            window_size = right - left + 1

            if window_size > minutes:
                if grumpy[left] == 1:
                    extra_saved -= customers[left]
                left += 1

            best_extra = max(best_extra, extra_saved)

        return baseline + best_extra


# -----------------------
# Test Cases
# -----------------------
sol = Solution()

customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy    = [0, 1, 0, 1, 0, 1, 0, 1]
minutes   = 3

print(sol.maxSatisfied(customers, grumpy, minutes))   # 16




#subarraysWithKDistinct


from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):

        def atMost(k):
            if k < 0:
                return 0

            count = defaultdict(int)
            left = 0
            result = 0

            for right in range(len(nums)):
                count[nums[right]] += 1

                while len(count) > k:
                    count[nums[left]] -= 1

                    if count[nums[left]] == 0:
                        del count[nums[left]]

                    left += 1

                result += right - left + 1

            return result

        return atMost(k) - atMost(k - 1)


# ---------------- Main Program ----------------

nums = [1, 2, 1, 2, 3]
k = 2

sol = Solution()
answer = sol.subarraysWithKDistinct(nums, k)

print("Number of subarrays with exactly", k, "distinct elements:", answer)

















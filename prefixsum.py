#IpivotIndex

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i

            left_sum += num

        return -1


# ---------------- Main Program ----------------

nums = [1, 7, 3, 6, 5, 6]

sol = Solution()
answer = sol.pivotIndex(nums)

print("Pivot Index:", answer)




#checkSubarraySum

class Solution:
    def checkSubarraySum(self, nums, k):
        # remainder -> earliest index where this remainder was seen
        remainder_index = {0: -1}

        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num

            if k != 0:
                remainder = current_sum % k
            else:
                remainder = current_sum

            if remainder in remainder_index:
                # Check if the subarray length is at least 2
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                # Store only the first occurrence of the remainder
                remainder_index[remainder] = i

        return False


# ---------------- Main Program ----------------

nums = [23, 2, 4, 6, 7]
k = 6

sol = Solution()
answer = sol.checkSubarraySum(nums, k)

print("Does a valid subarray exist?", answer)




#subarraySum

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num

            if (current_sum - k) in prefix_count:
                result += prefix_count[current_sum - k]

            prefix_count[current_sum] += 1

        return result


# ---------------- Main Program ----------------

nums = [1, 1, 1]
k = 2

sol = Solution()
answer = sol.subarraySum(nums, k)

print("Number of subarrays with sum", k, "=", answer)



#SUM RANGE 303
class NumArray:
    def __init__(self, nums):
        # prefix[i] = sum of nums[0..i-1]
        self.prefix = [0] * (len(nums) + 1)

        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


# -------------------------
# Test the class
# -------------------------

nums = [-2, 0, 3, -5, 2, -1]

numArray = NumArray(nums)

print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))


#runningSum

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []

        for num in nums:
            total += num
            result.append(total)

        return result


# -------------------------
# Test the solution
# -------------------------

nums = [1, 2, 3, 4]

sol = Solution()
answer = sol.runningSum(nums)

print(answer)




#findMaxLength
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_index_map = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in sum_index_map:
                max_len = max(max_len, i - sum_index_map[prefix_sum])
            else:
                sum_index_map[prefix_sum] = i

        return max_len


# -------------------------
# Test the solution
# -------------------------

nums = [0, 1]

sol = Solution()
answer = sol.findMaxLength(nums)

print(answer)



#subarraysDivByK
from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            remainder = current_sum % k

            result += prefix_count[remainder]
            prefix_count[remainder] += 1

        return result


# -------------------------
# Test the solution
# -------------------------

nums = [4, 5, 0, -2, -3, 1]
k = 5

sol = Solution()
answer = sol.subarraysDivByK(nums, k)

print(answer)



#numOfSubarrays


from collections import defaultdict
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        current_sum = 0
        result = 0

        for num in arr:
            current_sum += num
            parity = current_sum % 2

            if parity == 0:
                result += prefix_count[1]
            else:
                result += prefix_count[0]

            prefix_count[parity] += 1

        return result % MOD


# -------------------------
# Test the solution
# -------------------------

arr = [1, 3, 5]

sol = Solution()
answer = sol.numOfSubarrays(arr)

print(answer)




#minSumOfLengths
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        prefix_index = {0: -1}
        prefix_sum = 0
        answer = float('inf')
        min_length = float('inf')

        for i in range(n):
            prefix_sum += arr[i]

            if (prefix_sum - target) in prefix_index:
                start = prefix_index[prefix_sum - target] + 1
                length = i - start + 1

                if start > 0 and best[start - 1] != float('inf'):
                    answer = min(answer, length + best[start - 1])

                min_length = min(min_length, length)

            best[i] = min_length
            prefix_index[prefix_sum] = i

        return answer if answer != float('inf') else -1


# -------------------------
# Test the solution
# -------------------------

arr = [3, 2, 2, 4, 3]
target = 3

sol = Solution()
answer = sol.minSumOfLengths(arr, target)

print(answer)



#NumMatrix
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


# -------------------------
# Test the class
# -------------------------

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)

print(obj.sumRegion(2, 1, 4, 3))  # Expected: 8
print(obj.sumRegion(1, 1, 2, 2))  # Expected: 11
print(obj.sumRegion(1, 2, 2, 4))  # Expected: 12
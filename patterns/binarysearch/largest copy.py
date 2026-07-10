class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysNeeded(capacity):
            days_count = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    days_count += 1
                    current_load = w
                else:
                    current_load += w
            return days_count

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2
            if daysNeeded(mid) <= days:
                high = mid   # try smaller capacity
            else:
                low = mid + 1  # need bigger capacity

        return low
s1=Solution()
print(s1.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
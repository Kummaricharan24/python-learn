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
from collections import deque
from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            queue.append((tickets[i], i))

        time = 0

        while queue:
            count, index = queue.popleft()

            count -= 1
            time += 1

            if count == 0:
                if index == k:
                    return time
            else:
                queue.append((count, index))
# Driver Code
tickets = [2, 3, 2]
k = 2

obj = Solution()
result = obj.timeRequiredToBuy(tickets, k)

print(result)
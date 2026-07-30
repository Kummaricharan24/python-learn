import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        heap = [(0, 0)]      # (cost, starting point index)
        total_cost = 0

        while heap:
            cost, node = heapq.heappop(heap)

            if node in seen:
                continue

            seen.add(node)
            total_cost += cost

            # add all unvisited neighbors
            for j, point in enumerate(points):
                if j not in seen:
                    distance = abs(points[node][0] - point[0]) + abs(points[node][1] - point[1])
                    heapq.heappush(heap, (distance, j))

        return total_cost
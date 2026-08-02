import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fro, to, price in flights:
            graph[fro].append((to, price))

        heap = [(0, src, 0)]
        # best[city][stops] = cheapest cost to reach city using exactly 'stops' stops
        best = defaultdict(lambda: float('inf'))
        best[(src, 0)] = 0

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops <= k:
                for neighbour, price in graph[city]:
                    new_cost = cost + price
                    new_stops = stops + 1
                    if new_cost < best[(neighbour, new_stops)]:
                        best[(neighbour, new_stops)] = new_cost
                        heapq.heappush(heap, (new_cost, neighbour, new_stops))

        return -1
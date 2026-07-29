import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w  in times:
            graph[u].append((v,w))
        heap=[(0,k)]
        visited={}
        while heap:
            curr_dict,node=heapq.heappop(heap)
            if node in visited:
                continue 
            visited[node]=curr_dict
            for neighbour, weight in graph[node]:
                heapq.heappush(heap,(curr_dict+weight,neighbour))
        if len(visited) != n:
            return -1
        return max(visited.values())
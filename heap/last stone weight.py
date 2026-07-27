import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            first = -heapq.heappop(heap)
            secound = -heapq.heappop(heap)
            if first != secound:
                heapq.heappush(heap,-(first - secound))
        result = -heap[0] if heap else 0
        return result
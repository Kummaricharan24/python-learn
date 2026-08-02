import heapq
from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[]
        for task, freq in count.items():
            heapq.heappush(heap, (-freq , task))
        cooldown=deque()
        time=0
        while heap or cooldown:
            time+=1
            if cooldown and cooldown[0][2]==time:
                freq,task,available_time =cooldown.popleft()
                heapq.heappush(heap,(freq,task))
            if heap:
                freq,task=heapq.heappop(heap)
                freq+=1
                if freq!=0:
                    cooldown.append((freq, task, time + n + 1))
            else:
                pass
        return time

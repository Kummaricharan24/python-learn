from collections import deque
class RecentCounter:

    def __init__(self):
        self.recentcounter=deque()
        
    def ping(self, t: int) -> int:
        self.recentcounter.append(t)
        diff = t -3000
        if self.recentcounter[0] < diff:
            self.recentcounter.popleft()
        return len(self.recentcounter)
s1 = RecentCounter()

print(s1.ping(1))
print(s1.ping(100))
print(s1.ping(3001))
print(s1.ping(3002))
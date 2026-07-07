#meeting room
import heapq
from multiprocessing import heap
from typing import List


class solution:
    def class_attend_meeting(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
s1=solution()
print(s1.class_attend_meeting([[0,30],[5,10],[15,20]]))



#meeting room 2'
import heapq
class solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap=[]
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
s2=solution()
print(s2.minMeetingRooms([[0,30],[5,10],[15,20]]))  
        


#empoloyee free time
class solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        intervals = []
        for emp in schedule:
            for interval in emp:
                intervals.append(interval)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        free=[]
        for start, end in intervals[1:]:
            last=merged[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                free.append([last[1], start])
                merged.append([start, end])
        return free
s3=solution()
print(s3.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]))


#insert interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for start , end in intervals[1:]:
            last=result[-1]
            if start <=last[1]:
                last[1]=max(last[1],end)
            else:
                result.append([start,end])
        return result
s1=Solution()
print(s1.insert([[1,3],[6,9]],[2,5]))   
    

#overlapping intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])  # sort by END this time!
        count = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end          # keep this interval
            else:
                count += 1               # remove this one (it's the "worse" overlap)

        return count
s1=Solution()
print(s1.eraseOverlapIntervals([[1,2],[2,3],[3,4],[ 1,3]]))

#merge intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for start , end in intervals[1:]:
            last=result[-1]
            if start <=last[1]:
                last[1]=max(last[1],end)
            else:
                result.append([start,end])
        return result
s1=Solution()
print(s1.merge([[1,3],[2,6],[8,10],[15,18]]))
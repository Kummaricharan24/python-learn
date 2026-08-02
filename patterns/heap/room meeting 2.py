import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Sort meetings by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track end times of ongoing meetings
    heap = []

    for interval in intervals:
        start, end = interval[0], interval[1]

        # If the earliest ending meeting has already finished
        # before this one starts, reuse that room
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        # Add current meeting's end time to the heap
        heapq.heappush(heap, end)

    # The size of the heap = number of rooms in use simultaneously
    return len(heap)


# Test cases
print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # Output: 2
print(minMeetingRooms([[7, 10], [2, 4]]))              # Output: 1
print(minMeetingRooms([[0, 30], [5, 20]]))             # Output: 2
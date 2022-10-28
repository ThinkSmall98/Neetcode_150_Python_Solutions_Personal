# Time: O(n), Space: O(n)
from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        maxHeap = [-1 * i for i in count.values()]
        heapify(maxHeap)
        time = 0
        q = deque() # [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        return time
                

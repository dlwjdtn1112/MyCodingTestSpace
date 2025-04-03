import heapq

hq = []
heapq.heappush(hq, (2, 'apple'))
heapq.heappush(hq, (1, 'banana'))
heapq.heappush(hq, (2, 'orange'))

print(heapq.heappop(hq))  # 👉 (1, 'banana')

from queue import PriorityQueue

pq = PriorityQueue()
pq.put(3)
pq.put(1)
pq.put(5)

print(pq.get())

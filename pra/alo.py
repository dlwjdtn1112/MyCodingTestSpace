import heapq
import sys

input = sys.stdin.read
data_base = input().split()

a, b, c = int(data_base[0]), int(data_base[1]), int(data_base[2])

g1 = [[] for _ in range(a + 1)]
ind = 3
for _ in range(b):
    a = int(data_base[ind])

    b = int(data_base[ind + 1])

    c = int(data_base[ind + 2])
    g1[a].append((b, c))
    ind += 3

# Priority queues to store the k shortest paths to each node
pq = [[] for _ in range(a + 1)]
pq[1].append(0)

# Min-heap for Dijkstra's algorithm
h1 = [(0, 1)]  # (cost, node)

while h1:
    current_cost, current_node = heapq.heappop(h1)

    for neighbor, travel_cost in g1[current_node]:
        new_cost = current_cost + travel_cost

        if len(pq[neighbor]) < c:

            heapq.heappush(pq[neighbor], new_cost)
            heapq.heappush(h1, (new_cost, neighbor))
        elif pq[neighbor][0] > new_cost:
            heapq.heappushpop(pq[neighbor], new_cost)
            heapq.heappush(h1, (new_cost, neighbor))

# Output the k-th shortest paths
r1 = []
for i in range(1, a + 1):

    if len(pq[i]) < c:

        r1.append(-1)
    else:
        r1.append(heapq.heappop(pq[i]))

for result in r1:

    print(result)

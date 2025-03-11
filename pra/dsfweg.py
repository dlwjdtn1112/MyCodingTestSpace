from collections import deque

n = int(input())

arr = [list(map(int,input().split())) for i in range(n)]
for i in arr:
    print(*i)
print("-"*10)
l2 = zip(*arr)






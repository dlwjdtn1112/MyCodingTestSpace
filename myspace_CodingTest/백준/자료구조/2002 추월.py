l1 = []
l2 = []
l1_1 = []
from collections import deque
n = int(input())
l3 = deque()
for i in range(n):
    a = input()
    l1.append((a,i))
    l1_1.append(a)

d = deque(l1)

for i in range(n):
    a = input()
    l2.append(a)



while d:
    if d[0][0] == l2[0]:
        l3.append(d.popleft())
        l2.pop(0)
    else:
        d.append(d.popleft())

l3_1 = list(l3)


cnt = 0
for i in range(0,len(l3)):
    cnt1 = 0
    for j in range(i,len(l3)):
        if l3_1[i][1] > l3_1[j][1]:
            cnt1 += 1
    if cnt1 != 0:
        cnt+=1
print(cnt)
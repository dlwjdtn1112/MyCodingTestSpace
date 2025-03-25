N,M,K  = map(int,input().split())

l1 = list(map(int,input().split()))
l1_len = len(l1)
from collections import deque

l2 = deque(maxlen=M)
cnt = 1
l2.append(l1.pop(0))
l5 = []
if len(l1) == 0:
    l5.append(M)

else:
    while True:
        if sum(l2) + l1[0] > K:
            l2.append(0)
            cnt +=1
            if l2[0] != 0:
                l2.append(l1.pop(0))
                cnt +=1
                if len(l1) == 0:
                    cnt += (M)
                    break


        elif sum(l2) + l1[0] <= K:
            l2.append(l1.pop(0))
            cnt += 1
            if len(l1) == 0:
                cnt += (M)
                break




if len(l5) != 0:
    print(l5[0]+1)
else:
    print(cnt)
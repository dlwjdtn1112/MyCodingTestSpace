from collections import deque

result = []
n = int(input())
l1 = list(map(int,input().split()))
l1_deque = deque(l1)

m = int(input())
for _ in range(m):
    l2 = list(map(int,input().split()))
    l2_deque = deque(l2)
    for i in range(len(l2)):
        if l1_deque == l2_deque:
            result.append(l2)
            break
        else:
            l1_deque.append(l1_deque.popleft())

    else:
        l5 = []
        l3 = reversed(l2)
        for i in l3:
            if i == 3:
                l5.append(1)
            elif i == 1:
                l5.append(3)
            elif i == 4:
                l5.append(2)
            elif i == 2:
                l5.append(4)

        l5_deque = deque(l5)
        for i in range(len(l5)):
            if l1_deque == l5_deque:
                result.append(l2)
                break
            else:
                l5_deque.append(l5_deque.popleft())

print(len(result))
for i in result:
    print(*i)
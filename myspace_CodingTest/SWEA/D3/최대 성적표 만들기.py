n = int(input())
l1 = []
for i in range(n):
    cnt = 0
    a,b = map(int,input().split())
    l2=list(map(int,input().split()[:a]))
    l2.sort()
    l2.reverse()
    for i in range(b):
        cnt += l2[i]
    l1.append(cnt)
for i in range(n):
    print("#"+str(i+1), l1[i])
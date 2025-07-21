n = int(input())

l1 = []

for i in range(n):
    a = int(input())
    l2 = list(map(int,input().split()[:a*2]))
    cnt  = 0
    l3 = []
    while(True):
        if(l2[len(l2)-1]*(0.75)) in l2:
            l3.append(int(l2[len(l2)-1]*(0.75)))
            l2.remove(int(l2[len(l2)-1]*0.75))
            l2.remove(l2[len(l2)-1])
            cnt += 1
        if cnt == a:
            break
    l3.reverse()

    l1.append(l3)
v1 = 1
for i in l1:
    i = [str(j) for j in i]
    print("#"+str(v1)," ".join(i))
    v1 += 1
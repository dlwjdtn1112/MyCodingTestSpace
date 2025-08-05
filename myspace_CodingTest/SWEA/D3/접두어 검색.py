

result = []

T = int(input())
cnt1 = 0
for _ in range(T):

    cnt2 = 0
    l1 = []
    l2 = []
    a,b = map(int,input().split())
    for i in range(a):
        l1.append(input())
    for i in range(b):
        l2.append(input())

    for lst1 in l2:
        cnt1 = 0
        for lst2 in l1:
            if lst2.startswith(lst1) == True:
                cnt1 += 1
        if cnt1 != 0:
            cnt2 += 1
    result.append(cnt2)


for i in range(len(result)):
    print("#"+str(i+1), result[i])






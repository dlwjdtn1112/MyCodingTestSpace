result = []

n = int(input())

for _ in range(n):
    a,b,c = map(int,input().split())
    l1 = list(map(int,input().split()))

    for i in range(b):
        x,y = map(int,input().split())
        l1.insert(x,y)
    result.append(l1[c])

for  i in range(len(result)):
    print("#"+str(i+1) , result[i])
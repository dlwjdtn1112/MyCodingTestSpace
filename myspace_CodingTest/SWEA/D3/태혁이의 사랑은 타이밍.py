

result = []

T = int(input())

for _ in range(T):
    a,b,c = map(int,input().split())
    cnt = 0

    if (a,b,c) == (11,11,11):
        result.append(0)
    elif (a,b,c) < (11,11,11):
        result.append(-1)
    else:
        result.append((a - 11) * 1440 + (b - 11) * 60 + (c - 11))


for i in range(len(result)):
    print("#"+str(i+1) , result[i])
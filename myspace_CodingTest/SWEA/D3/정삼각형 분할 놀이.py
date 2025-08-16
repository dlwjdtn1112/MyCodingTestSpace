

result = []

T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    result.append((a**2)//(b**1))

for i in range(len(result)):
    print("#"+str(i+1) , result[i])
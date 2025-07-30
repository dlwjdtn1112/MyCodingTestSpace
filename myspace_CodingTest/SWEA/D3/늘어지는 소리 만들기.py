result = []

T = int(input())

for _ in range(T):
    s = list(input())
    n = int(input())
    arr = list(map(int,input().split()[:n]))
    arr.sort()

    # s.insert(arr[0]+0,'-')
    # s.insert(arr[1]+1, '-')
    # s.insert(arr[2]+2, '-')
    for i in range(len(arr)):
        s.insert(arr[i]+i,'-')

    result.append("".join(s))

for i in range(len(result)):
    print("#"+str(i+1), result[i])


# 내가 작성한 코드
N = int(input())
result = []

for _ in range(N):

    a = int(input())
    l2 = []
    arr = list(map(int,input().split()[:a]))
    for i in range(1,len(arr)):
        l1 = []
        cnt = 0
        l1.append(arr[0])
        for j in range(1,len(arr)):
            if i == j and i < len(arr)-1 and  j < len(arr)-1:
                pass
            else:
                l1.append(arr[j])


        for lst in range(1,len(l1)):
            cnt += abs(l1[lst] - l1[lst-1])
        l2.append(cnt)
    l2.pop(-1)
    result.append(min(l2))

for lst in result:
    print(lst)


#chat gpt
N = int(input())
result = []

for _ in range(N):

    a = int(input())
    l2 = []
    arr = list(map(int,input().split()[:a]))
    for i in range(1,len(arr)):
        l1 = []
        cnt = 0
        l1.append(arr[0])
        for j in range(1,len(arr)):
            if i == j and i < len(arr)-1 and  j < len(arr)-1:
                pass
            else:
                l1.append(arr[j])


        for lst in range(1,len(l1)):
            cnt += abs(l1[lst] - l1[lst-1])
        l2.append(cnt)
    l2.pop(-1)
    result.append(min(l2))

for lst in result:
    print(lst)











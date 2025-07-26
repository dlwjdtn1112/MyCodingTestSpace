
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
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 원래 총 거리 계산
    total = 0
    for i in range(1, N):
        total += abs(arr[i] - arr[i-1])

    # 중간 지점 하나 생략할 경우 최솟값 갱신
    min_dist = float('inf')
    for skip in range(1, N - 1):  # 2번~N-1번 (index 1~N-2)
        removed = abs(arr[skip] - arr[skip - 1]) + abs(arr[skip + 1] - arr[skip])
        added = abs(arr[skip + 1] - arr[skip - 1])
        new_total = total - removed + added
        min_dist = min(min_dist, new_total)

    print(min_dist)











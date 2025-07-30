# 내가 작성한 코드
result = []
n = int(input())

for _ in range(n):
    arr = []
    a,b = map(int,input().split())
    l1 = list(map(int,input().split()[:a]))
    l2 = list(map(int, input().split()[:b]))

    for lst in l1:
        if lst in l2:
            arr.append(lst)
    for lst1 in l2:
        if lst1 in l1:
            arr.append(lst1)

    result.append(len(set(arr)))


for i in range(len(result)):
    print("#"+str(i+1), result[i])


# chat gpt4o

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    # 교집합 개수 계산
    intersection_count = len(A & B)

    print(f"#{t} {intersection_count}")

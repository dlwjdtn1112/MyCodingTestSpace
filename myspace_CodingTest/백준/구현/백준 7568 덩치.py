
#내가 작성한 코드
N = int(input())

arr = []
result = []
for i in range(N):
    arr.append(list(map(int,input().split())))



for i in range(len(arr)):
    status = 1
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            if arr[j][0]  > arr[i][0] and arr[j][1] > arr[i][1]:
                status += 1

    result.append(str(status))

print(" ".join(result))
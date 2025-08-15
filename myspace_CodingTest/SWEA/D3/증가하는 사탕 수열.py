result = []

T = int(input())

for _ in range(T):
    cnt = 0
    arr = list(map(int, input().split()))

    if arr[2] > arr[1] and arr[1] > arr[0]:
        result.append(0)

    else:
        while True:
            if arr[2] <= arr[1]:
                arr[1] -= 1
                cnt += 1
            else:
                break
        while True:
            if arr[1] <= arr[0]:
                arr[0] -= 1
                cnt += 1
            else:
                break
        # if arr[0] > 0 and arr[1] > 0 and arr[2] > 0:
        #     result.append(cnt)
        # else:
        #     result.append(-1)

        if all(i > 0 for i in arr) == True:
            result.append(cnt)
        else:
            result.append(-1)

for i in range(len(result)):
    print("#" + str(i + 1), result[i])

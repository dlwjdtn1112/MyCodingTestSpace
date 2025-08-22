
result = []

T = int(input())

for _ in range(T):
    state = 0
    l1 = []
    stop = [0 for i in range(200)]
    current = 0
    cnt = 0
    cnt_power = 0
    a ,b ,c = map(int ,input().split())
    arr = list(map(int ,input().split()))
    for i in arr:
        stop[i] = 'o'
    for i in range(1 ,len(arr)):
        if arr[i] -arr[i - 1] > a:
            state = 1
            break

    if state == 1:
        result.append(0)
    elif state == 0:
        for k in range(c):
            for i in range(a):
                current += 1
                if stop[current] == 'o':
                    cnt_power = current
            current = cnt_power
            if cnt_power + a >= b:
                cnt += 1
                break
            cnt += 1
        result.append(cnt)

for i in range(len(result)):
    print("#" + str(i + 1), result[i])


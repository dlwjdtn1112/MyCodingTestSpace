

# from itertools import permutations
#
# T = int(input())
# result = []
#
# for _ in range(T):
#     a = int(input())
#
#     l1 = []
#     arr0 = [i for i in range(a)]
#     arr1 = list(permutations(arr0,a))
#
#     arr = [list(map(int,input().split())) for _ in range(a)]
#     for lst in arr1:
#         cnt1 = 0
#         cnt = 0
#         for i in lst:
#             cnt += arr[cnt1][i]
#             cnt1 += 1
#         l1.append(cnt)
#     result.append(min(l1))
#
# for i in range(len(result)):
#     print("#"+str(i+1) , result[i])


from itertools import permutations

T = int(input().strip())
result = []

for _ in range(T):
    a = int(input().strip())
    arr0 = [i for i in range(a)]
    arr = [list(map(int, input().split())) for _ in range(a)]

    min_sum = float('inf')  # 최소값을 무한대로 초기화

    # 제너레이터 사용
    arr1 = permutations(arr0, a)

    for lst in arr1:
        current_sum = 0

        # 가지치기: 현재 합이 최소값보다 커지면 더 이상 계산할 필요 없음
        if current_sum >= min_sum:
            continue

        for i in range(a):
            current_sum += arr[i][lst[i]]
            # 중간에 합이 min_sum보다 커지면 break
            if current_sum >= min_sum:
                break

        # for-else 문을 사용하면 break 없이도 가능
        else:
            min_sum = min(min_sum, current_sum)

    result.append(min_sum)

for i in range(len(result)):
    print("#" + str(i + 1), result[i])





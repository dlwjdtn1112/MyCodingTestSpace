



# N = int(input())
#
#
# arr1 = []
# arr2 = []
#
# l1 = list(map(int,input().split()))
# l1.sort()
# for i in l1:
#     cnt = 0
#     for j in l1:
#         if i - j > 0:
#             cnt += i-j
#         else:
#             cnt += j-i
#     arr1.append(i)
#     arr2.append(cnt)
# print(arr2.index(min(arr2)) + 1)



N = int(input())

arr = list(map(int,input().split()))
arr.sort()
if len(arr) % 2 == 0:
    print(arr[N // 2 -1])
else:
    print(arr[N // 2])











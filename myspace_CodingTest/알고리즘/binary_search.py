
# ✅ 예제: bisect_left와 bisect_right의 차이

import bisect

arr = [1, 3, 3, 5, 7, 9]

x = 3

left_idx = bisect.bisect_left(arr, x)
right_idx = bisect.bisect_right(arr, x)

print(f"bisect_left: {left_idx}")   # 3이 처음 나타나는 위치
print(f"bisect_right: {right_idx}") # 3보다 큰 값이 처음 나타나는 위치

# ✅ 예제: 정렬된 리스트에 값을 정렬 유지하면서 삽입

import bisect

arr = [1, 2, 4, 5]
bisect.insort(arr, 3)  # 3을 알맞은 위치에 삽입
print(arr)  # [1, 2, 3, 4, 5]



# ✅ 특정 값이 리스트에 존재하는지 체크 (bisect_left 응용)
import bisect

def binary_search(arr, x):
    idx = bisect.bisect_left(arr, x)
    if idx < len(arr) and arr[idx] == x:
        return idx
    else:
        return -1

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 7))  # 3
print(binary_search(arr, 4))  # -1

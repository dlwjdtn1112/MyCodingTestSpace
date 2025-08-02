import heapq

# 초기 리스트
nums = [5, 3, 8, 1, 2, 9]

# 리스트를 최소 힙으로 변환
heapq.heapify(nums)

print("Heapified:", nums)  # 내부적으로 힙 구조를 만족하는 리스트

# 최소값 꺼내기
min_val = heapq.heappop(nums)
print("Min value:", min_val)
print("Heap after pop:", nums)

# 값 추가
heapq.heappush(nums, 4)
print("Heap after push:", nums)


# Heapified: [1, 2, 8, 3, 5, 9]
# Min value: 1
# Heap after pop: [2, 3, 8, 9, 5]
# Heap after push: [2, 3, 4, 9, 5, 8]

# heapfy를 사용하면 sort()함수 없이
# 최대값 최솟값 구하는것이 가능하고, 효율적이다.
# 세 개의 그릇 무게를 입력받습니다.
weights = []

# 무게 입력 받기
for i in range(3):
    weight = int(input())
    weights.append(weight)

# 무게 정렬
weights.sort()

# 중간 무게 출력 (Mama Bear의 그릇 무게)
mama_bear_weight = weights[1]
print( mama_bear_weight)
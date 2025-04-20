
#chat gpt4o
# 정수 x 입력
x = int(input())

# DP 테이블 초기화 (0으로 시작, 1 ~ x까지)
d = [0] * 30001

# 보텀업 방식으로 DP 수행
for i in range(2, x + 1):
    # 1을 빼는 연산
    d[i] = d[i - 1] + 1

    # 2로 나누어 떨어질 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    # 3으로 나누어 떨어질 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    # 5로 나누어 떨어질 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

# 정답 출력
print(d[x])

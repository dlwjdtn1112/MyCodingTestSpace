
result = []
n = int(input())

for _ in range(n):
    a = int(input())
    b = list(input())
    b_set = list(set(b))
    ##b_set.sort()


    if len(b) == 2:
        if len(b_set) == 1:
            result.append("Yes")
        else:
            result.append("No")
    elif len(b) % 2 != 0:
        result.append("No")

    else:
        cnt  = len(b) // 2
        s1 = "".join(b)
        s2 = "".join(b[0:cnt]) * 2
        if s1 == s2:
            result.append("Yes")
        else:
            result.append("No")

for i in range(len(result)):
    print("#"+str(i+1) + " " +result[i])



# Gemini
# 결과를 저장할 리스트
results = []

# 테스트 케이스의 개수 N을 입력 받음
N = int(input())

# 각 테스트 케이스를 반복 처리
for i in range(N):
    # 각 테스트 케이스의 첫 번째 줄 (문자열 길이, 여기서는 'a' 변수로 받지만 사용하지 않음)
    _ = int(input())

    # 두 번째 줄 (알파벳 소문자 문자열 b)
    b = input()

    # 1. 길이 조건 확인: 문자열의 길이가 홀수이면 절대 S+S 형태가 될 수 없음
    if len(b) % 2 != 0:
        results.append("No")
    else:
        # 2. 내용 조건 확인: 문자열을 정확히 절반으로 나누어 앞 절반과 뒤 절반이 동일한지 확인
        half_length = len(b) // 2
        first_half = b[0:half_length]
        second_half = b[half_length:len(b)]  # 또는 b[half_length:]

        if first_half == second_half:
            results.append("Yes")
        else:
            results.append("No")

# 모든 테스트 케이스의 결과를 출력
for i in range(len(results)):
    print(f"#{i + 1} {results[i]}")












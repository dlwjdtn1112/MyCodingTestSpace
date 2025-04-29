
# 내가 작성한 코드(시간 초과 ㅠ ㅠ)
def solution(sequence, k):
    result = []

    for i in range(len(sequence)):
        cnt = 0
        cnt += sequence[i]
        if sequence[i] == k:
            result.append((i,i))
        else:
            for j in range(i + 1, len(sequence)):
                if cnt + sequence[j] == k:
                    result.append((i, j))
                elif cnt + sequence[j] > k:
                    break
                else:
                    cnt += sequence[j]

    result1 = []
    result2 = []
    for lst in result:
        result1.append(list(lst))

    for lst in result1:
        lst.append(lst[1]-lst[0])
        result2.append(lst)

    result_final = sorted(result2,key=lambda x:(x[2],x[0]))
    result_final[0].pop(2)
    return result_final[0]

# 다시 한번 내가 작성한 코드 (투 포인터 알고리즘 ^^)

def solution2(sequence, k):
    result3 = []
    interval_sum = 0
    count = 0
    end = 0
    for i in range(len(sequence)):
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1

        if interval_sum == k:
            count += 1
            result3.append((i,end-1))
        interval_sum -= sequence[i]

    result4 = []
    result_final = []

    for lst in result3:
        result4.append(list(lst))

    for lst in result4:
        lst.append(lst[1]-lst[0])

    result_final = sorted(result4,key=lambda x:(x[2],x[0]))

    result_final[0].pop(2)
    return result_final[0]

# chat gpt4o
def solution3(sequence, k):
    n = len(sequence)
    left = 0
    right = 0
    total = sequence[0]

    answer = []
    min_len = float('inf')

    while left <= right and right < n:
        if total < k:
            right += 1
            if right < n:
                total += sequence[right]
        elif total > k:
            total -= sequence[left]
            left += 1
        else:
            # total == k
            if right - left < min_len:
                min_len = right - left
                answer = [left, right]

            # 윈도우 줄이기
            total -= sequence[left]
            left += 1

    return answer








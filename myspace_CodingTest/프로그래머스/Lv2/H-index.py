# 내가 작성한 코드(정확도 87.5)
def solution1(citations):
    cnt = 0
    arr = citations
    ans = 0

    while True:
        cnt1 = 0
        for i in arr:
            if i >= cnt:
                cnt1 += 1
            else:
                pass
        if cnt == cnt1:
            ans = cnt
            break
        else:
            cnt += 1

        if cnt >= len(arr):
            break

    return ans

# chat gpt4o
def solution2(citations):
    citations.sort(reverse=True)  # 인용 수 많은 순으로 정렬
    for i, cite in enumerate(citations):
        if cite <= i:
            return i
    return len(citations)

# 내가 작성한 코드
def solution(prices):
    result = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        result.append(cnt)

    return result
# ChatGPT 4o
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # 스택의 top보다 현재 가격이 낮으면 가격이 떨어진 거임
        while stack and prices[stack[-1]] > price:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    # 스택에 남은 애들 = 끝까지 가격 안 떨어진 경우
    for idx in stack:
        answer[idx] = len(prices) - 1 - idx

    return answer









# 내가 작성한 코드
def solution(seoul):
    index1 = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            index1 = i

    answer = '김서방은 '  + str(index1) + '에 있다'
    return answer

seoul = ["Jane", "Kim"]
print(solution(seoul))
# chat gpt4o
def solution2(seoul):
    index = seoul.index("Kim")
    return f"김서방은 {index}에 있다"

print(solution2(seoul))
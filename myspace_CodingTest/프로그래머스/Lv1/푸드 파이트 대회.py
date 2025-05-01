# 내가 작성한 코드
def solution1(food):
    result = ""

    for i in range(1, len(food)):
        c = food[i] // 2
        result += str(i) * c

    result_list = list(result)
    result_list.reverse()
    result2 = "".join(result_list)

    result += "0"
    result += result2

    return result

# chat gpt4o
def solution2(food):
    left = []
    for i in range(1, len(food)):
        left.append(str(i) * (food[i] // 2))

    half = ''.join(left)
    return half + '0' + half[::-1]

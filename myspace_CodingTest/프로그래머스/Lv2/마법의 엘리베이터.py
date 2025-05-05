
# 내가 작성한 코드
def solution1(storey):
    stone = 0
    while storey:
        num1 = storey % 10
        num10 = (storey % 100) // 10

        if num1 < 5:
            stone += num1
        elif num1 == 5:
            if num10 < 5:
                stone += num1
            elif num10 > 5:
                stone += (10-num1)
                storey += 10

        elif num1 > 5:
            stone += (10-num1)
            storey += 10
        storey = storey // 10
    return stone



#chat gpt4o

def solution2(storey):
    result = 0

    while storey > 0:
        digit_s = storey % 10
        next_digit = (storey // 10) % 10

        if digit_s > 5 or (digit_s == 5 and next_digit > 5):
            result += 10 - digit_s
            storey += 10
        else:
            result += digit_s

        storey //= 10

    return result

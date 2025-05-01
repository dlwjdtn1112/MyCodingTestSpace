#내가 작성한 코드

def solutio1(s):
    result = []

    cnt = 0
    cnt_zero = 0
    while True:
        s1 = list(s)
        cnt_zero += s1.count("0")

        for i in range(s1.count("0")):
            s1.remove("0")

        cnt += 1

        s1_len = len(s1)
        s1_bin = bin(s1_len)[2:]
        if str(s1_bin) == "1":
            result.append(cnt)
            result.append(cnt_zero)
            break
        else:
            s = str(s1_bin)
    return result


#chat gpt4o
def solutio2(s):
    result = []

    cnt = 0
    cnt_zero = 0
    while True:
        cnt_zero += s.count("0")
        s = s.replace("0", "")

        cnt += 1

        s1_len = len(s)
        s1_bin = bin(s1_len)[2:]
        if s1_bin == "1":
            result.append(cnt)
            result.append(cnt_zero)
            break
        else:
            s = s1_bin
    return result

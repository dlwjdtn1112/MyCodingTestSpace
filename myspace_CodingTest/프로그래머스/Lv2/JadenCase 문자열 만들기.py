def solution(s):
    s1 = s.split(" ")
    result = ""
    for lst in s1:
        if lst == "":
            result += " "
        elif lst[0].isalpha():
            result += lst[0].upper()
            for i in range(1, len(lst)):
                if lst[i].isupper():
                    result += lst[i].lower()
                else:
                    result += lst[i]
            result += " "
        else:
            result += lst.lower() + " "

    return result[:-1]  # 마지막 공백 제거


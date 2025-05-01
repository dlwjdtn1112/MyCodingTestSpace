def solution(phone_number):
    answer = ''
    phone_number_list = list(phone_number)

    for i in range(len(phone_number_list) - 4):
        phone_number_list[i] = "*"

    answer = "".join(phone_number_list)
    return answer
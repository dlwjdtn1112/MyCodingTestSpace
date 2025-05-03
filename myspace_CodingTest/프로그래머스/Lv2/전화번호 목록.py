

#내가 작성한 코드
def solution1(phone_book):
    result = "true"
    for lst1 in range(len(phone_book) - 1):
        for lst2 in range(lst1 + 1, len(phone_book)):
            if phone_book[lst1] == phone_book[lst2]:
                continue
            elif phone_book[lst1] == phone_book[lst2][0:len(phone_book[lst1])]:
                result = "false"
                break
    return result == "true"

#chat gpt4o
def solution2(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


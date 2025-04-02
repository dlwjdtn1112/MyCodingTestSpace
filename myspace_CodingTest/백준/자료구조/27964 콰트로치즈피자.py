# 내가 작성한 코드
N = int(input())

arr = list(input().split())
result = []
for lst in arr:
    lst += "l"
    if lst[-7:-1] == "Cheese":
        result.append(lst)

if (len(set(result)))  > 3:
    print("yummy")
else:
    print("sad")

# 개선된 코드(Chat gpt)

# 토핑의 개수 입력
n = int(input())

# 토핑 목록 입력
toppings = input().split()

# 'Cheese'로 끝나는 서로 다른 토핑을 저장할 집합
cheese_toppings = set()

# 각 토핑 확인
for topping in toppings:
    if topping.endswith('Cheese'):
        cheese_toppings.add(topping)

# 결과 출력
if len(cheese_toppings) >= 4:
    print("yummy")
else:
    print("sad")






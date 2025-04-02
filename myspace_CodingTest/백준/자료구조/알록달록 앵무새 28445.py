from itertools import permutations

# 내가 작성한 코드
color_l1 = []

a,b = input().split()
color_l1.append(a)
color_l1.append(b)

c,d = input().split()
color_l1.append(c)
color_l1.append(d)

s = set(color_l1)

result = list(permutations(s,2))

for i in s:
    result.append((i,i))


result1 = sorted(result,key = lambda x:(x[0],x[1]))

for lst in result1:
    print(*lst)

# 개선된 코드(chat gpt)
# 색상 입력 받기
fBody, fTail = input().split()
mBody, mTail = input().split()

# 중복을 제거한 색상 리스트 생성
colors = sorted(set([fBody, fTail, mBody, mTail]))

# 모든 색상 조합 출력
for color1 in colors:
    for color2 in colors:
        print(color1, color2)
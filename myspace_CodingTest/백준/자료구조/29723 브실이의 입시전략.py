# 내가 작성한 코드
a,b,c = map(int,input().split())
arr = []
arr1 = []
for i in range(a):
    l1  = list(input().split())
    l1[1] = int(l1[1])
    arr.append(l1)
cnt = 0

for i in range(c):
    arr1.append(input())
for i in arr1:
    for j in arr:
        if i == j[0]:
            cnt += j[1]
            arr.remove(j)


arr_s = sorted(arr,key=lambda x:x[1])



max1 = cnt
min1 = cnt

for i in range(b-c):
    min1 += arr_s[i][1]
arr_s.reverse()

for i in range(b-c):
    max1  += arr_s[i][1]
print(min1,max1)

# chatGPT4o(개선된 코드)
n, m, k = map(int, input().split())

subject_scores = {}
for _ in range(n):
    name, score = input().split()
    subject_scores[name] = int(score)

known_subjects = [input() for _ in range(k)]

# 공개된 과목 점수 합산
base_score = sum(subject_scores[name] for name in known_subjects)

# 공개되지 않은 과목 리스트
remaining_scores = [score for name, score in subject_scores.items() if name not in known_subjects]

# 최소 점수: 낮은 점수부터 m-k개 선택
min_score = base_score + sum(sorted(remaining_scores)[:m-k])

# 최대 점수: 높은 점수부터 m-k개 선택
max_score = base_score + sum(sorted(remaining_scores, reverse=True)[:m-k])

print(min_score, max_score)


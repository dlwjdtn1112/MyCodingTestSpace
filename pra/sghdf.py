import sys
import math


def cross(o, a, b):
    """ 벡터 OA x OB 의 외적값(실수)을 반환 """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """
    앤드류 알고리즘을 이용해 주어진 점들의 볼록껍질을 구해서
    (반시계방향)으로 이뤄진 리스트를 반환
    """
    # x좌표, y좌표 오름차순 정렬
    points = sorted(points)

    # 아래껍질(lower hull)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # 위껍질(upper hull)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # 맨 마지막 점은 중복이므로 제거
    lower.pop()
    upper.pop()

    # 볼록껍질 정점 리스트 (반시계 방향)
    return lower + upper


def dist(a, b):
    """ 두 점 (a,b) 사이의 유클리드 거리 """
    return math.hypot(a[0] - b[0], a[1] - b[1])


def rotating_calipers(hull):
    """
    회전 캘리퍼 기법으로 볼록껍질 hull 에서
    모든 점을 포함하는 직사각형(임의각도) 중 최소 둘레를 구한다.
    리턴값: 최소 둘레(실수)

    ※ 알고리즘 개요:
      - hull의 모든 변에 대해, 그 변을 x축과 평행하다고 보고
      - 이때의 직사각형 (min/max x, min/max y)을 찾고 둘레 계산
      - 이 과정을 hull의 변 수(=H)만큼 반복
      - O(H) 로 처리 가능.
    """
    # 볼록껍질 점 수
    n = len(hull)
    if n == 1:
        # 점이 하나뿐이면, 둘레 = 0
        return 0.0
    elif n == 2:
        # 점이 두 개뿐이면, 선분 하나만 존재
        return 2.0 * dist(hull[0], hull[1])  # 사각형이라기보단 선분의 양끝 포함

    # '다각형의 각 변'을 기준으로 회전시키며 검사
    k = 1
    l = 1
    r = 1

    min_perim = float('inf')

    for i in range(n):
        # i번째 점과 i+1 (모듈로)점이 이루는 변
        i_next = (i + 1) % n
        # 현재 변 벡터
        dx = hull[i_next][0] - hull[i][0]
        dy = hull[i_next][1] - hull[i][1]

        # 변의 길이
        edge_len = math.hypot(dx, dy)

        # 회전각도를 직접 구하기보다는, dot/외적을 이용해 다른 점들의 min/max를 찾는 식
        # 여기서는 앤티포달 포인트를 업데이트 하는 전형적 기법을 사용

        # 1) top(최대 y방향) 갱신
        while abs(cross(hull[i], hull[i_next], hull[(k + 1) % n])) > \
                abs(cross(hull[i], hull[i_next], hull[k])):
            k = (k + 1) % n

        # 2) right(최대 x방향) 갱신
        while (dx * (hull[(r + 1) % n][1] - hull[i][1]) - dy * (hull[(r + 1) % n][0] - hull[i][0])) > \
                (dx * (hull[r][1] - hull[i][1]) - dy * (hull[r][0] - hull[i][0])):
            r = (r + 1) % n

        # 3) left(최소 x방향) 갱신
        while (dx * (hull[(l + 1) % n][1] - hull[i][1]) - dy * (hull[(l + 1) % n][0] - hull[i][0])) < \
                (dx * (hull[l][1] - hull[i][1]) - dy * (hull[l][0] - hull[i][0])):
            l = (l + 1) % n

        # 이제 i번째 변과 평행/수직 방향에서 사각형의 '폭'과 '높이'를 구함
        # (dx, dy)는 변벡터 이고, edge_len = 변 길이
        # (dx/edge_len, dy/edge_len)는 변벡터의 방향단위
        # 그에 수직인 단위벡터는 (-dy/edge_len, dx/edge_len)

        # '가로' 길이 = r과 l이 주는 거리차
        # '세로' 길이 = k가 주는 최대 높이
        # 여기서 실제로는 cross, dot 등을 활용해 길이를 구해야 함

        # 가로 거리(= x방향 거리)
        #   dot((hull[r] - hull[i]), (dx, dy)) - dot((hull[l] - hull[i]), (dx, dy)) 전체 / edge_len
        # 세로 거리(= y방향 거리)
        #   cross((hull[i_next] - hull[i]), (hull[k] - hull[i])) / edge_len

        # 벡터 hr = (hull[r].x - hull[i].x, hull[r].y - hull[i].y)
        # 벡터 hl = (hull[l].x - hull[i].x, hull[l].y - hull[i].y)
        # 가로길이 = [(hr ⋅ (dx,dy)) - (hl ⋅ (dx,dy))] / edge_len

        hrx, hry = hull[r][0] - hull[i][0], hull[r][1] - hull[i][1]
        hlx, hly = hull[l][0] - hull[i][0], hull[l][1] - hull[i][1]
        horizontal = (hrx * dx + hry * dy - (hlx * dx + hly * dy)) / edge_len

        # 세로길이 = cross((dx,dy), (hull[k]-hull[i])) / edge_len
        #           = abs( cross((hull[i_next]-hull[i]), (hull[k]-hull[i])) ) / edge_len
        hkx, hky = hull[k][0] - hull[i][0], hull[k][1] - hull[i][1]
        vertical = abs(dx * hky - dy * hkx) / edge_len

        cur_perim = 2.0 * (abs(horizontal) + abs(vertical))
        min_perim = min(min_perim, cur_perim)

    return min_perim


def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    points = []
    for _ in range(N):
        x, y = map(float, input().split())
        points.append((x, y))

    # 특수 케이스 처리
    if N == 1:
        # 점 하나 -> 둘레=0
        print(0)
        return
    elif N == 2:
        # 점 두 개 -> 그은 직사각형은 결국 선분
        p1, p2 = points
        ans = 2.0 * dist(p1, p2)  # 사실상 선분을 '직사각형'으로 보면 한 변은 0
        # 문제 요구: 최종값 * 2 뒤 정수 변환
        print(int(ans * 2))
        return

    # 볼록껍질 구하기
    hull = convex_hull(points)

    # 최소둘레 구하기
    min_perim = rotating_calipers(hull)

    # 문제 요구: "최종값에서 곱하기 2를 하도록 하고 그 다음 정수형으로 변환"
    #          = int(min_perim * 2)
    result = int(min_perim * 2)

    print(result)


if __name__ == "__main__":
    solve()



l1 = list(map(int,input().split()))



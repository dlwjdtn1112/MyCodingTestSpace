NUM = 50
skip = [0] * NUM

def index(c):
    # 알파벳 대문자만 들어온다고 가정
    if ord(c) >= 65:
        return ord(c) - 65
    elif c == " ":  # 공백문자가 들어왔을 경우의 처리
        return 26
    else:
        return ord(c)

def init_skip(p):
    """
    주어진 패턴 문자열을 기반으로 skip 배열을 초기화하는 함수

    :param p: 패턴 문자열
    """
    global skip
    M = len(p)  # 패턴의 길이

    for i in range(NUM):
        skip[i] = M  # 패턴에 없는 문자면 패턴 문자열 길이만큼 skip

    for i in range(M):
        skip[index(p[i])] = M - i - 1  # 패턴에 있는 문자면 패턴의 끝과 그 문자와의 거리만큼 skip

def mis_char(p, t):
    """
    주어진 패턴과 텍스트에서 패턴이 발생한 위치를 찾는 함수

    :param p: 패턴 문자열
    :param t: 텍스트 문자열
    :return: 패턴이 발생한 위치
    """
    global skip
    M = len(p)  # 패턴의 길이
    N = len(t)  # 텍스트의 길이
    i = M - 1  # 텍스트 문자열의 인덱스
    j = M - 1  # 패턴 문자열의 인덱스

    init_skip(p)

    # 패턴의 오른쪽 끝에서부터 비교 시작
    while j >= 0:
        while t[i] != p[j]:
            # skip 배열의 특정 알파벳에 해당하는 인덱스 위치의 값을 k에 집어넣는다.
            # 만약 t[i]의 문자가 패턴 안에 있는 문자라면 skip 배열의 해당 문자의 skip 거리를 집어넣고,
            # 없다면 패턴의 길이인 M을 넣는다.
            k = skip[index(t[i])]

            if M - j > k:  # 패턴의 길이 - 비교해서 맞은 수가 k보다 크면
                i += M - j  # 패턴의 길이 - 비교해서 맞은 수 만큼 오른쪽으로 가서 비교
            else:  # 그렇지 않으면 k만큼 오른쪽으로 가서 비교
                i += k

            if i >= N:  # 끝까지 비교를 완료하면 N을 반환
                return N

            # 패턴이 일치할 경우 왼쪽으로 계속 비교하면서 j값이 작아지는데,
            # 이 때, 불일치 발생시(t[i] != p[j]) 다시 j를 M - 1로 초기화
            j = M - 1

        i -= 1
        j -= 1

    return i + 1

def main():
    text = "VISION QUESTION ONION CAPTION GRADUATION EDUCATION"
    pattern = "ATION"

    k = 0
    while k < len(text):
        pos = mis_char(pattern, text[k:])
        pos += k  # 이전에 찾은 k값(pos + M)을 더해주고
        k = pos + len(pattern)  # k값 업데이트
        if k <= len(text):  # k가 N보다 작거나 같다면, 즉 패턴이 text의 끝부분까지 존재한다면
            print("패턴이 발생한 위치:", pos)

    print("\n정보통신공학과 12171850 정연한")

if __name__ == "__main__":
    main()

    main()



def solution(x):
    x_str = list(str(x))
    x_str2 = [int(i) for i in x_str]

    if x % sum(x_str2) == 0:
        return True
    else:
        return False
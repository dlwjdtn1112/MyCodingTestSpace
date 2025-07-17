
def solution_my(s):
    answer  = False

    s = str(s)
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        answer = True


    return answer



def solution(s):
    bracket = 0
    for i in s:
        if i == "(":
            bracket += 1
        else:
            bracket -= 1
        if bracket < 0:
            return False
    if bracket != 0:
        return False
    return True
        